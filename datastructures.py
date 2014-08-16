#!/usr/bin/python3
# coding: utf-8
#
# datastructures.py, (c) 2014, Immanuel Albrecht; mail@immanuel-albrecht.de
#
# This program is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program. If not, see <http://www.gnu.org/licenses/>.
#

import sys,os,time
import uuid
import array

def strap(s):
    x = ""
    for c in s:
        if not c.isspace():
            return x
        x += c
    return x

def fill_up(s,l):
    if len(s) >= l:
        return s
    return s + " "*(l-len(s))

def do_sort(a):
    s = [x for x in a]
    s.sort()
    return s

def short_id():
    return uuid.uuid4().hex.upper()[0:6]

def kill_newline(x):
    if x.endswith("\r\n"):
        return x[:-2]
    if x.endswith("\n") or x.endswith("\r"):
        return x[:-1]
    return x

def delim_spacer(x):
    x = x.replace("\t"," ").replace("\n"," ").replace("\r"," ").strip()
    while 1:
        y = x.replace("  "," ")
        if x == y:
            return x
        x = y

def strip_C(x):
    if x.endswith(".C") or x.endswith(".c") or x.endswith(".h") or x.endswith(".h"):
        return x[:-2]
    return x

def strip_PY(x):
    if x.upper().endswith(".PY"):
        return x[:-3]
    return x

def new_struct(name):
    s = {}
    s["TYPES"] = []
    s["NAMES"] = []
    s["STRUCT"] = name;
    s["OPTIONS"] = []
    s["options"] = []
    return s;

C_types = {}
C_types["INT8"] = "int8_t"
C_types["INT16"] = "int16_t"
C_types["INT32"] = "int32_t"
C_types["INT64"] = "int64_t"
C_types["UINT8"] = "uint8_t"
C_types["UINT16"] = "uint16_t"
C_types["UINT32"] = "uint32_t"
C_types["UINT64"] = "uint64_t"
C_types["FLOAT"] = "float"
C_types["DOUBLE"] = "double"
C_types["CHAR"] = "char"

sizeof = {}
sizeof["INT8"] = 1
sizeof["INT16"] = 2
sizeof["INT32"] = 4
sizeof["INT64"] = 8
sizeof["UINT8"] = 1
sizeof["UINT16"] = 2
sizeof["UINT32"] = 4
sizeof["UINT64"] = 8
sizeof["FLOAT"] = 4
sizeof["DOUBLE"] = 8
sizeof["CHAR"] = 1

PY_types = {}
PY_types["INT8"] = "0"
PY_types["INT16"] = "0"
PY_types["INT32"] = "0"
PY_types["INT64"] = "0"
PY_types["UINT8"] = "0"
PY_types["UINT16"] = "0"
PY_types["UINT32"] = "0"
PY_types["UINT64"] = "0"
PY_types["FLOAT"] = "0.0"
PY_types["DOUBLE"] = "0.0"
PY_types["CHAR"] = "chr(0)"

PY_converts = {}
PY_converts["INT8"] = "int"
PY_converts["INT16"] = "int"
PY_converts["INT32"] = "int"
PY_converts["INT64"] = "int"
PY_converts["UINT8"] = "int"
PY_converts["UINT16"] = "int"
PY_converts["UINT32"] = "int"
PY_converts["UINT64"] = "int"
PY_converts["FLOAT"] = "float"
PY_converts["DOUBLE"] = "float"
PY_converts["CHAR"] = "str"

PY_arrays = {}
PY_arrays["INT8"] = "array.array('b')"
PY_arrays["INT16"] = "array.array('h')"
PY_arrays["INT32"] = "array.array('l')"
PY_arrays["INT64"] = "[]"
PY_arrays["UINT8"] = "array.array('B')"
PY_arrays["UINT16"] = "array.array('H')"
PY_arrays["UINT32"] = "array.array('L')"
PY_arrays["UINT64"] = "[]"
PY_arrays["FLOAT"] = "array.array('f')"
PY_arrays["DOUBLE"] = "array.array('d')"
PY_arrays["CHAR"] = "\"\""

# take care of 64bit vs 32bit; i.e. check int length
check_array = array.array('I')
check_array.append(0)
if len(check_array.tobytes()) == 4:
    PY_arrays["INT32"] = "array.array('i')"
    PY_arrays["UINT32"] = "array.array('I')"
check_array = array.array('L')
check_array.append(0)
if len(check_array.tobytes()) == 8:
    PY_arrays["INT64"] = "array.array('l')"
    PY_arrays["UINT64"] = "array.array('L')"

# struct has standard sizes by prefix =
PY_struct_codes = {}
PY_struct_codes["INT8"] = "=b"
PY_struct_codes["INT16"] = "=h"
PY_struct_codes["INT32"] = "=l"
PY_struct_codes["INT64"] = "=q"
PY_struct_codes["UINT8"] = "=B"
PY_struct_codes["UINT16"] = "=H"
PY_struct_codes["UINT32"] = "=L"
PY_struct_codes["UINT64"] = "=Q"
PY_struct_codes["FLOAT"] = "=f"
PY_struct_codes["DOUBLE"] = "=d"
PY_struct_codes["CHAR"] = "=c"

def add_member(struct, line, LINE):
    IN = LINE.split(" ")
    if IN[0] == "C" or IN[0] == "PYTHON":
        return #output file spec
    if IN[0] == "ARRAY": #array
        if IN[1] in C_types:
            ins = line.split(" ")
            field = ins[2]
            if field in struct["NAMES"]:
                print("Error: Field ",field," defined twice!")
            else:
                struct["TYPES"].append( (IN[0],IN[1],) )
                struct["NAMES"].append(field)
                struct["OPTIONS"].append(IN[3:])
                struct["options"].append(ins[3:])
                
        else:
            print("Error: Type ARRAY ",IN[1]," unknown!")
    elif IN[0] == "STRUCT": #pointer to some other structure
        ins = line.split(" ")
        structname = ins[1]
        field = ins[2]
        if field in struct["NAMES"]:
            print("Error: Field ",field," defined twice!")
        else:
            struct["TYPES"].append( (IN[0],structname,) )
            struct["NAMES"].append(field)
            struct["OPTIONS"].append(IN[3:])
            struct["options"].append(ins[3:])
    elif IN[0] == "STRING": # C string handling
        ins = line.split(" ")
        field = ins[1]
        if field in struct["NAMES"]:
            print("Error: Field ",field," defined twice!")
        else:
            struct["TYPES"].append( (IN[0],"",) )
            struct["NAMES"].append(field)
            struct["OPTIONS"].append(IN[2:])
            struct["options"].append(ins[2:])
    elif IN[0].startswith("["):
        if IN[1] in C_types:
            ins = line.split(" ")
            field = ins[2]
            if field in struct["NAMES"]:
                print("Error: Field ",field," defined twice!")
            else:
                struct["TYPES"].append( (IN[0],IN[1],) )
                struct["NAMES"].append(field)
                struct["OPTIONS"].append(IN[3:])
                struct["options"].append(ins[3:])
        else:
            print("Error: Type",IN[0]," ",IN[1]," unknown!")
    else:
        if IN[0] in C_types:
            ins = line.split(" ")
            field = ins[1]
            if field in struct["NAMES"]:
                print("Error: Field ", field," defined twice!")
            else:
                struct["TYPES"].append( ("",IN[0],) )
                struct["NAMES"].append(field)
                struct["OPTIONS"].append(IN[2:])
                struct["options"].append(ins[2:])
        else:
            print("Error: Type ",IN[0]," unknown!")

def H_once(contents, name):
    candidates = []
    line = 0
    for x in contents:
        if x.strip().startswith("#ifndef"):
            toks = delim_spacer(x).split(" ")
            if len(toks)>1:
                candidates.append(toks[1])
        elif x.strip().startswith("#define"):
            toks = delim_spacer(x).split(" ")
            if len(toks)>1:
                if toks[1] in candidates:
                    return toks[1],line
        line += 1
    token = "__"+os.path.basename(name).upper()+"_H_"+short_id()
    contents.append("#ifndef "+token)
    line += 1
    contents.append("#define "+token)
    contents.append("")
    contents.append("#endif //"+token)
    return token,line

def H_guarded_lines(contents, token):
    line = 0
    start = 0
    depth = 0
    for x in contents:
        if x.strip().startswith("#define"):
            toks = delim_spacer(x).split(" ")
            if len(toks)>1:
                if (toks[1] == token):
                    depth = 1
                    start = line+1
        elif x.strip().startswith("#endif"):
            depth -= 1
            if depth == 0:
                return start,line-1
        elif x.strip().startswith("#if"):
            depth += 1
        line += 1
    #something's wrong here. Nevermind.
    return start,line

def C_include(contents, include_token):
    last_include = -1
    line = 0
    for x in contents:
        if x.strip().startswith("#include"):
            last_include = line
            toks = delim_spacer(x).split(" ")
            if len(toks)>1:
                if (toks[1] == include_token):
                    return line
        line += 1
    contents.insert(last_include+1,"#include "+include_token)
    contents.insert(last_include+2,"")

    return last_include+1

def H_include(contents, include_token, token):
    line = 0
    start,stop = H_guarded_lines(contents, token)
    last_include = start
    for x in contents:
        if x.strip().startswith("#include"):
            last_include = line
            toks = delim_spacer(x).split(" ")
            if len(toks)>1:
                if (toks[1] == include_token):
                    return line
        line += 1
        if line > stop:
            break


    contents.insert(last_include+1,"#include "+include_token)
    contents.insert(last_include+2,"")

    return last_include+1

def H_define(contents, identifier, replacement, token):
    line = 0
    start,stop = H_guarded_lines(contents, token)
    last_include = start
    last_define = start
    for x in contents:
        if x.strip().startswith("#include"):
            last_include = line
        elif x.strip().startswith("#define"):
            last_define = line
            toks = delim_spacer(x).split(" ")
            if len(toks)>1:
                if (toks[1] == identifier):
                    contents[line] = "#define "+identifier+" "+replacement
                    return line
        line += 1
        if line > stop:
            break

    if last_include > last_define:
        last_define = last_include
    
    contents.insert(last_define+1,"#define "+identifier+" "+replacement)
    contents.insert(last_define+2,"")

    return last_define+1

def H_typedef_struct(contents,struct,token):
    line = 0
    start,stop = H_guarded_lines(contents, token)
    start_token = -1
    for x in contents:
        if x.strip().startswith("typedef"):
            # typedef struct t_*** ...
            toks = delim_spacer(x).split(" ")
            if len(toks)>2:
                if (toks[1] == "struct") and (toks[2] == "t_"+struct["STRUCT"]):
                    start_token = line
                    break
        line += 1
        if line > stop:
            break
    no_closing_delim = 0
    if start_token == -1:
        start_token = stop+1
    else:
        stop_token = start_token-1
        while 1:
            stop_token += 1
            if stop_token == stop:
                break
            if x.strip().startswith("}"):
                break
            elif (delim_spacer(x).upper().find("END OF AUTO")>=0):
                no_closing_delim = 1
                break

        for i in range(start_token,stop_token+1):
            contents.pop(start_token)

    generated = []

    generated.append("typedef struct t_"+struct["STRUCT"]+" {")
    generated.append(" /* Automatically generated code.")
    generated.append("  * Do not edit manually as all changes will be lost!")
    generated.append("  * Generated "+time.strftime("%c"))
    generated.append("  */ ")
    generated.append("")

    used_fields = []

    idx = 0
    for idx in range(len(struct["NAMES"])):
        t0, t1 = struct["TYPES"][idx]
        field = struct["NAMES"][idx]
        if field in used_fields:
            print("Error: Tried to use field twice: ",field)
        else:
            used_fields.append(field)
            if t0 == "ARRAY":
                if (field+"_N") in used_fields:
                    print("Error: Tried to use field twice: ",field+"_N")
                else:
                    used_fields.append(field+"_N")
                    generated.append("    int32_t "+field+"_N;")
                    generated.append("    "+C_types[t1]+" *"+field+"; /* points to an array of "+C_types[t1]+"["+field+"_N] */")
            elif t0 == "STRUCT":
                generated.append("    "+t1+" "+field+";")
            elif t0 == "STRING":
                generated.append("    char *"+field+";")
            elif t0.startswith("["):
                generated.append("    "+C_types[t1]+" "+field+t0+";")
            else:
                generated.append("    "+C_types[t1]+" "+field+";")
    

    generated.append("")
    generated.append(" /* End of automatically generated code. Manual editing below is safe. */")

    if no_closing_delim == 0:
        generated.append(" } s_"+struct["STRUCT"]+";")
        generated.append("");

    for x in range(len(generated)):
        contents.insert(x+start_token, generated[x])

def H_typedef_pointer(contents,struct,token):
    line = 0
    start,stop = H_guarded_lines(contents, token)
    for x in contents:
        if delim_spacer(x).replace(" ","").startswith("typedefs_"+struct["STRUCT"]+"*"+struct["STRUCT"]+";"):
            return
        line += 1
        if line > stop:
            contents.insert(line,"typedef s_"+struct["STRUCT"]+" *"+struct["STRUCT"]+";");
            contents.insert(line+1,"");
            return

def H_forward_decl(contents,decl,token,shortened=0):
    if shortened == 0:
        shortened = decl
    decl_cmp = delim_spacer(shortened).strip()
    start,stop = H_guarded_lines(contents,token)
    for idx in range(start,stop+1):
        if delim_spacer(contents[idx]).strip().startswith(decl):
            contents.pop(idx)
            contents.insert(idx,decl+" /* Do not edit this line. */");
            return

    contents.insert(stop+1,decl+" /* Do not edit this line. */");
    contents.insert(stop+2,"")

def H_alloc_free(contents,struct,token):
    T = struct["STRUCT"]
    array_list = ""
    for idx in range(len(struct["NAMES"])):
        if struct["TYPES"][idx][0] == "ARRAY" and not "NOALLOC" in struct["OPTIONS"][idx]:
            if array_list != "":
                array_list += ", "
            array_list += "int32_t N_"+struct["NAMES"][idx]

    H_forward_decl(contents,T+" "+T+"_alloc("+array_list+");",token,T+" "+T+"_alloc(");
    H_forward_decl(contents,"void "+T+"_free("+T+" x);",token);


def C_alloc(contents, struct):
    T = struct["STRUCT"]
    array_list = ""
    for idx in range(len(struct["NAMES"])):
        if struct["TYPES"][idx][0] == "ARRAY" and not "NOALLOC" in struct["OPTIONS"][idx]:
            if array_list != "":
                array_list += ", "
            array_list += "int32_t N_"+struct["NAMES"][idx]

    start = -1
    start_delim = T+" "+T+"_alloc(";
    for line in range(len(contents)):
        if delim_spacer(contents[line]).strip().startswith(start_delim):
            start = line
            break
    no_closing_delim = 0
    if start == -1:
        contents.append("")
        start = len(contents)
    else:
        for line in range(start,len(contents)):
            if contents[line].strip().startswith("}"):
                stop = line
                break
            elif delim_spacer(contents[line]).upper().find("END OF AUTO") >= 0:
                stop = line
                no_closing_delim = 1
                break
        for i in range(start,stop+1):
            contents.pop(start)

    generated = []
    generated.append(T+" "+T+"_alloc("+array_list+")")
    generated.append("{ /* Automatically generated code.")
    generated.append("   * Do not edit manually as all changes will be lost!")
    generated.append("   * Generated "+time.strftime("%c"))
    generated.append("   */ ")
    generated.append("")
    generated.append("    "+T+" x = calloc(1, sizeof(s_"+T+"));")
    generated.append("    assert(x);")
    generated.append("")

    for idx in range(len(struct["NAMES"])):
        if struct["TYPES"][idx][0] == "ARRAY" and not "NOALLOC" in struct["OPTIONS"][idx]:
            F = struct["NAMES"][idx]
            generated.append("    x->"+F+"_N = N_"+F+";")
            generated.append("    x->"+F+" = calloc(x->"+F+"_N, sizeof("+C_types[struct["TYPES"][idx][1]]+"));")
            generated.append("    assert(x->"+F+");")
            generated.append("")
        elif struct["TYPES"][idx][0] == "STRING" and not "NOALLOC" in struct["OPTIONS"][idx]:
            F = struct["NAMES"][idx]
            generated.append("    x->"+F+" = strdup(\"\");")
            generated.append("")


    generated.append("")
    generated.append("   /* End of automatically generated code. Manual editing below is safe. */")

    if no_closing_delim == 0:
        generated.append("")
        generated.append("    return x;")
        generated.append("}")
        generated.append("")

    for x in range(len(generated)):
        contents.insert(x+start, generated[x])

def C_free(contents, struct):
    T = struct["STRUCT"]

    start = -1
    start_delim = "void "+T+"_free(";
    for line in range(len(contents)):
        if delim_spacer(contents[line]).strip().startswith(start_delim):
            start = line
            break
    no_closing_delim = 0
    if start == -1:
        contents.append("")
        start = len(contents)
    else:
        for line in range(start,len(contents)):
            if contents[line].strip().startswith("}"):
                stop = line
                break
            elif delim_spacer(contents[line]).upper().find("END OF AUTO") >= 0:
                stop = line
                no_closing_delim = 1
                break
        for i in range(start,stop+1):
            contents.pop(start)

    generated = []
    generated.append("void "+T+"_free("+T+" x)")
    generated.append("{ /* Automatically generated code.")
    generated.append("   * Do not edit manually as all changes will be lost!")
    generated.append("   * Generated "+time.strftime("%c"))
    generated.append("   */ ")
    generated.append("")

    for idx in range(len(struct["NAMES"])):
        if struct["TYPES"][idx][0] == "ARRAY":
            if not "NOFREE" in struct["OPTIONS"][idx]:
                F = struct["NAMES"][idx]
                generated.append("    if (x->"+F+") free(x->"+F+");")
                generated.append("")
        elif struct["TYPES"][idx][0] == "STRING":
            if not "NOFREE" in struct["OPTIONS"][idx]:
                F = struct["NAMES"][idx]
                generated.append("    if (x->"+F+") free(x->"+F+");")
        elif struct["TYPES"][idx][0] == "STRUCT":
            if not "NOFREE" in struct["OPTIONS"][idx]:
                F = struct["NAMES"][idx]
                T = struct["TYPES"][idx][1]
                generated.append("    if (x->"+F+") "+T+"_free(x->"+F+");")

    generated.append("")
    generated.append("   /* End of automatically generated code. Manual editing below is safe. */")

    if no_closing_delim == 0:
        generated.append("")
        generated.append("    free(x);")
        generated.append("}")
        generated.append("")

    for x in range(len(generated)):
        contents.insert(x+start, generated[x])

def H_io(contents,struct,token):
    T = struct["STRUCT"]
    H_forward_decl(contents,T+" "+T+"_alloc_from_file(FILE *f);",token);
    H_forward_decl(contents,"void "+T+"_write_to_file("+T+" x, FILE *f);",token);

def IO_coding(struct):
    code = ""
    for (t0,t1),opts in zip(struct["TYPES"],struct["OPTIONS"]):
        if "NOI/O" in opts:
            continue
        if code != "":
            code += "|"
        code += t0+" "+t1;
        if t0 == "STRING" and "CI/O" in opts:
            code += "CI/O";
    return code

def C_alloc_from_file(contents, struct):
    T = struct["STRUCT"]

    start = -1
    start_delim = T+" "+T+"_alloc_from_file(";
    for line in range(len(contents)):
        if delim_spacer(contents[line]).strip().startswith(start_delim):
            start = line
            break
    no_closing_delim = 0
    if start == -1:
        contents.append("")
        start = len(contents)
    else:
        nested = 1
        for line in range(start,len(contents)):
            if contents[line].strip().startswith("}"):
                nested -= 1
                if nested == 0:
                    stop = line
                    break
            elif contents[line].strip().endswith("{"):
                nested += 1
            elif delim_spacer(contents[line]).upper().find("END OF AUTO") >= 0:
                stop = line
                no_closing_delim = 1
                break
        for i in range(start,stop+1):
            contents.pop(start)

    generated = []
    generated.append(T+" "+T+"_alloc_from_file(FILE *f)")
    generated.append("{ /* Automatically generated code.")
    generated.append("   * Do not edit manually as all changes will be lost!")
    generated.append("   * Generated "+time.strftime("%c"))
    generated.append("   */ ")

    for (t0,t1),opts in zip(struct["TYPES"],struct["OPTIONS"]):
        if "NOI/O" in opts:
            continue;
        if t0 == "STRING":
            generated.append("    int32_t len;")
            break
    for (t0,t1),opts in zip(struct["TYPES"],struct["OPTIONS"]):
        if "NOI/O" in opts:
            continue;
        if t0 == "STRING" and "CI/O" in opts:
            generated.append("    char cio_buffer[MAX_CIO_SIZE];")
            generated.append("    int cio_idx;")
            generated.append("    char c;")
            break

    generated.append("    "+T+" x;");


    if not( "UNSAFE_IO" in struct ):
        CODE = IO_coding(struct)
        generated.append("    static const char io_code[] = \""+CODE+"\";")
        generated.append("    char io_check["+str(len(CODE)+1)+"];")
        generated.append("")
        generated.append("    fread(io_check,sizeof(char),"+str(len(CODE))+",f);")
        generated.append("    io_check["+str(len(CODE))+"] = 0;")
        generated.append("    if (strcmp(io_check, io_code)) return 0; /* incompatible file contents */")
        generated.append("")

    generated.append("")
    generated.append("    x = calloc(1, sizeof(s_"+T+"));")
    generated.append("    assert(x);")
    generated.append("")
        

    for idx in range(len(struct["NAMES"])):
        if "NOI/O" in struct["OPTIONS"][idx]:
            continue
        if struct["TYPES"][idx][0] == "ARRAY":
            F = struct["NAMES"][idx]
            T = C_types[struct["TYPES"][idx][1]]
            generated.append("    fread(&x->"+F+"_N, sizeof(int32_t), 1, f);")
            generated.append("    x->"+F+" = calloc(x->"+F+"_N, sizeof("+T+"));")
            generated.append("    assert(x->"+F+");")
            generated.append("    fread(x->"+F+", sizeof("+T+"), x->"+F+"_N, f);")
            generated.append("")
        elif struct["TYPES"][idx][0] == "STRING":
            if "CI/O" in opts:
                F = struct["NAMES"][idx]
                generated.append("    cio_idx = 0;");
                generated.append("    c = 1;");
                generated.append("    while (c != 0) {");
                generated.append("        c = 0;")
                generated.append("        fread(&c, sizeof(char), 1, f);")
                generated.append("        cio_buffer[cio_idx] = c;")
                generated.append("        if (cio_idx < MAX_CIO_SIZE) cio_idx++;")
                generated.append("    }")
                generated.append("    x->"+F+" = strdup(cio_buffer);")
            else:
                F = struct["NAMES"][idx]
                generated.append("    fread(&len, sizeof(int32_t), 1, f);")
                generated.append("    x->"+F+" = calloc(len+1, sizeof(char));")
                generated.append("    assert(x->"+F+");")
                generated.append("    fread(x->"+F+", sizeof(char), len, f);")
                generated.append("    x->"+F+"[len] = 0;")
                generated.append("")
        elif struct["TYPES"][idx][0] == "":
            F = struct["NAMES"][idx]
            T = C_types[struct["TYPES"][idx][1]]
            generated.append("    fread(&x->"+F+", sizeof("+T+"), 1, f);")
            generated.append("")
        elif struct["TYPES"][idx][0] == "STRUCT":
            F = struct["NAMES"][idx]
            T = struct["TYPES"][idx][1]
            generated.append("    x->"+F+" = "+T+"_alloc_from_file(f);")
            generated.append("")
        elif struct["TYPES"][idx][0].startswith("["):
            F = struct["NAMES"][idx]
            t0 = struct["TYPES"][idx][0]
            generated.append("    fread(&x->"+F+", sizeof(x->"+F+"), 1, f);")
            if "CSAFE" in struct["OPTIONS"][idx]:
                generated.append("    x->"+F+"["+str(int(t0[1:-1])-1)+"] = 0;")
            generated.append("")



    generated.append("")
    generated.append("   /* End of automatically generated code. Manual editing below is safe. */")

    if no_closing_delim == 0:
        generated.append("")
        generated.append("    return x;")
        generated.append("}")
        generated.append("")

    for x in range(len(generated)):
        contents.insert(x+start, generated[x])

def C_write_to_file(contents, struct):
    T = struct["STRUCT"]

    start = -1
    start_delim = "void "+T+"_write_to_file(";
    for line in range(len(contents)):
        if delim_spacer(contents[line]).strip().startswith(start_delim):
            start = line
            break
    no_closing_delim = 0
    if start == -1:
        contents.append("")
        start = len(contents)
    else:
        for line in range(start,len(contents)):
            if contents[line].strip().startswith("}"):
                stop = line
                break
            elif delim_spacer(contents[line]).upper().find("END OF AUTO") >= 0:
                stop = line
                no_closing_delim = 1
                break
        for i in range(start,stop+1):
            contents.pop(start)

    generated = []
    generated.append("void "+T+"_write_to_file("+T+" x, FILE *f)")
    generated.append("{ /* Automatically generated code.")
    generated.append("   * Do not edit manually as all changes will be lost!")
    generated.append("   * Generated "+time.strftime("%c"))
    generated.append("   */ ")
    generated.append("    assert(x);")
    generated.append("")

    for (t0,t1),opts in zip(struct["TYPES"],struct["OPTIONS"]):
        if "NOI/O" in opts:
            continue
        if t0 == "STRING":
            generated.append("    int32_t len;")
            generated.append("")
            break


    if not( "UNSAFE_IO" in struct ):
        CODE = IO_coding(struct)
        generated.append("    static const char io_code[] = \""+CODE+"\";")
        generated.append("")
        generated.append("    fwrite(io_code,sizeof(char),"+str(len(CODE))+",f);")
        generated.append("")

        

    for idx in range(len(struct["NAMES"])):
        if "NOI/O" in struct["OPTIONS"][idx]:
            continue
        if struct["TYPES"][idx][0] == "ARRAY":
            F = struct["NAMES"][idx]
            T = C_types[struct["TYPES"][idx][1]]
            generated.append("    fwrite(&x->"+F+"_N, sizeof(int32_t), 1, f);")
            generated.append("    fwrite(x->"+F+", sizeof("+T+"), x->"+F+"_N, f);")
            generated.append("")
        elif struct["TYPES"][idx][0] == "STRING":
            F = struct["NAMES"][idx]
            generated.append("    assert(x->"+F+");")
            generated.append("    len = strlen(x->"+F+");")
            if not "CI/O" in struct["OPTIONS"][idx]:
                generated.append("    fwrite(&len, sizeof(int32_t), 1, f);")
                generated.append("    fwrite(x->"+F+", sizeof(char), len, f);")
            else:
                generated.append("    fwrite(x->"+F+", sizeof(char), len+1, f);")
            generated.append("")
        elif struct["TYPES"][idx][0] == "":
            F = struct["NAMES"][idx]
            T = C_types[struct["TYPES"][idx][1]]
            generated.append("    fwrite(&x->"+F+", sizeof("+T+"), 1, f);")
            generated.append("")
        elif struct["TYPES"][idx][0] == "STRUCT":
            F = struct["NAMES"][idx]
            T = struct["TYPES"][idx][1]
            generated.append("    assert(x->"+F+");")
            generated.append("    "+T+"_write_to_file(x->"+F+",f);")
            generated.append("")
        elif struct["TYPES"][idx][0].startswith("["):
            F = struct["NAMES"][idx]
            T = C_types[struct["TYPES"][idx][1]]
            t0 = struct["TYPES"][idx][0]
            if "CSAFE" in struct["OPTIONS"][idx]:
                generated.append("    x->"+F+"["+str(int(t0[1:-1])-1)+"] = 0;")
            generated.append("    fwrite(&x->"+F+", sizeof(x->"+F+"), 1, f);")
            generated.append("")


    generated.append("")
    generated.append("   /* End of automatically generated code. Manual editing below is safe. */")

    if no_closing_delim == 0:
        generated.append("")
        generated.append("}")
        generated.append("")

    for x in range(len(generated)):
        contents.insert(x+start, generated[x])

def H_cmp(contents,struct,token):
    T = struct["STRUCT"]
    H_forward_decl(contents,"int "+T+"_cmp("+T+" l, "+T+" r);",token);

def C_cmp(contents, struct):
    T = struct["STRUCT"]

    start = -1
    start_delim = "int "+T+"_cmp(";
    for line in range(len(contents)):
        if delim_spacer(contents[line]).strip().startswith(start_delim):
            start = line
            break
    no_closing_delim = 0
    if start == -1:
        contents.append("")
        start = len(contents)
    else:
        nested_depth = 1
        for line in range(start,len(contents)):
            if contents[line].strip().startswith("}"): #CAREFUL HERE :) !!
                nested_depth -= 1
                if (nested_depth == 0):
                    stop = line
                    break
            elif contents[line].strip().endswith("{"):
                nested_depth += 1
            elif delim_spacer(contents[line]).upper().find("END OF AUTO") >= 0:
                stop = line
                no_closing_delim = 1
                break
        for i in range(start,stop+1):
            contents.pop(start)

    generated = []
    generated.append("int "+T+"_cmp("+T+" l, "+T+" r)")
    generated.append("{ /* Automatically generated code.")
    generated.append("   * Do not edit manually as all changes will be lost!")
    generated.append("   * Generated "+time.strftime("%c"))
    generated.append("   */ ")
    generated.append("")

    for (t0,t1),opts in zip(struct["TYPES"],struct["OPTIONS"]):
        if "NOCMP" in opts:
            continue
        if (t0 == "STRUCT") or (t0 == "STRING"):
            generated.append("    int cmp;")
            generated.append("")
            break

    for (t0,t1),opts in zip(struct["TYPES"],struct["OPTIONS"]):
        if "NOCMP" in opts:
            continue
        if (t0 == "ARRAY") or (t0.startswith("[")):
            generated.append("    int32_t i, N;")
            generated.append("")
            break



    generated.append("    if (r == l) return 0;")
    generated.append("    if (l == 0) return -1;")
    generated.append("    if (r == 0) return 1;")
    generated.append("")

        

    for idx in range(len(struct["NAMES"])):
        if "NOCMP" in struct["OPTIONS"][idx]:
            continue
        if struct["TYPES"][idx][0] == "ARRAY":
            F = struct["NAMES"][idx]
            generated.append("    if (l->"+F+"_N < r->"+F+"_N) return -1;") 
            generated.append("    if (r->"+F+"_N < l->"+F+"_N) return 1;") 
            generated.append("")
            generated.append("    N = l->"+F+"_N;")
            generated.append("    for (i = 0; i < N; ++i) {")
            generated.append("        if (l->"+F+"[i] < r->"+F+"[i]) return -1;")
            generated.append("        if (r->"+F+"[i] < l->"+F+"[i]) return 1;")
            generated.append("    }")
            generated.append("")
        elif struct["TYPES"][idx][0].startswith("["):
            F = struct["NAMES"][idx]
            generated.append("    N = sizeof(l->"+F+")/sizeof("+C_types[struct["TYPES"][idx][1]]+");")
            generated.append("    for (i = 0; i < N; ++i) {")
            generated.append("        if (l->"+F+"[i] < r->"+F+"[i]) return -1;")
            generated.append("        if (r->"+F+"[i] < l->"+F+"[i]) return 1;")
            generated.append("    }")
            generated.append("")
        elif struct["TYPES"][idx][0] == "STRING":
            F = struct["NAMES"][idx]
            generated.append("    if (l->"+F+" == 0)")
            generated.append("    {")
            generated.append("        if (r->"+F+" != 0) return 1;")
            generated.append("    } else if (r->"+F+" == 0) return -1;")
            generated.append("    else {")
            generated.append("        cmp = strcmp(l->"+F+", r->"+F+");")
            generated.append("        if (cmp != 0) return cmp;")
            generated.append("    }")
            generated.append("")
        elif struct["TYPES"][idx][0] == "":
            F = struct["NAMES"][idx]
            generated.append("    if (l->"+F+" < r->"+F+") return -1;") 
            generated.append("    if (r->"+F+" < l->"+F+") return 1;") 
            generated.append("")
        elif struct["TYPES"][idx][0] == "STRUCT":
            F = struct["NAMES"][idx]
            T = struct["TYPES"][idx][1]
            generated.append("    if (l->"+F+" == 0)")
            generated.append("    {")
            generated.append("        if (r->"+F+" != 0) return 1;")
            generated.append("    } else if (r->"+F+" == 0) return -1;")
            generated.append("    else {")
            generated.append("        cmp = "+T+"_cmp(l->"+F+", r->"+F+");")
            generated.append("        if (cmp != 0) return cmp;")
            generated.append("    }")
            generated.append("")


    generated.append("")
    generated.append("   /* End of automatically generated code. Manual editing below is safe. */")

    if no_closing_delim == 0:
        generated.append("")
        generated.append("    return 0;")
        generated.append("}")
        generated.append("")

    for x in range(len(generated)):
        contents.insert(x+start, generated[x])

def update_C(filename, struct):
    contents_C = []
    contents_H = []
    if os.path.exists(filename+".c"):
        f = open(filename+".c", encoding="utf-8")
        contents_C = [kill_newline(x) for x in f.readlines()]
        f.close()
    if os.path.exists(filename+".h"):
        f = open(filename+".h", encoding="utf-8")
        contents_H = [kill_newline(x) for x in f.readlines()]
        f.close()

    # make sure the header is def-guarded
    once_token, defline = H_once(contents_H,filename)

    # include C types
    H_include(contents_H, "<stdint.h>", once_token)
    H_include(contents_H, "<stdio.h>", once_token)
    H_define(contents_H, "MAX_CIO_SIZE", "1025", once_token)

    # typedefs
    H_typedef_struct(contents_H, struct, once_token)
    H_typedef_pointer(contents_H, struct, once_token)

    # memory management etc.
    H_alloc_free(contents_H, struct, once_token)
    H_io(contents_H, struct, once_token)
    H_cmp(contents_H, struct, once_token)

    # make sure the header file is included
    incline = C_include(contents_C, "\"%s.h\""%os.path.basename(filename))

    # other includes needed
    C_include(contents_C,"<assert.h>")
    C_include(contents_C,"<stdlib.h>")
    C_include(contents_C,"<string.h>")

    # function bodies
    C_alloc(contents_C,struct)
    C_free(contents_C,struct)
    C_alloc_from_file(contents_C,struct)
    C_write_to_file(contents_C,struct)
    C_cmp(contents_C,struct)


    f = open(filename+".c","w",encoding="utf-8")
    for l in contents_C:
        f.write(l+"\n")
    f.close()
    f = open(filename+".h","w",encoding="utf-8")
    for l in contents_H:
        f.write(l+"\n")
    f.close()

def PY_header(contents):
    if not len(contents) or not contents[0].startswith("#!"):
        contents.insert(0,"#!/usr/bin/python3 -i ")
    if len(contents)<2 or contents[1].find("utf-8") < 0:
        contents.insert(1,"# coding: utf-8")
        contents.insert(2,"")

def PY_mark(contents):
    line = 0
    for x in contents:
        y = x.strip().upper()
        if -1 < y.find("#") < y.find("GENERATED") < y.find("CODE") < y.find("ABOVE"):
            return line
        line += 1
    line = len(contents)
    contents.append("# All generated code will be placed above this mark.")
    contents.append("")

    return line


def PY_def(contents, name, params, head, tail):
    starts = -1
    line = 0
    for x in contents:
        if delim_spacer(x).startswith("def "+name):
            starts = line
            break
        line += 1
    if starts == -1:
        contents.append("")
        starts = len(contents)
        contents.append("def "+name+"():")
        contents.append("")
    
    delims = strap(contents[line+1])
    if delims == "": #we also fix wrong python code :)
        delims = "    "
        ends = starts+1
    else:
        for i in range(starts+1,len(contents)):
            if contents[i].startswith(delims):
                ends = i+1
            elif contents[i].strip() != "":
                break

    current_blocks = contents[starts:ends]
    is_manual = 0
    mid_part = []
    for y in current_blocks:
        x = y.upper()
        if -1 < x.find("#") < x.find("END") < x.find("MANUAL") < x.find("EDIT"):
            is_manual = 0
        if is_manual:
            mid_part.append(y)
        if -1 < x.find("#") < x.find("BEGIN") < x.find("MANUAL") < x.find("EDIT"):
            is_manual = 1

    if len(mid_part) == 0:
        mid_part.append(delims)

    generated = []
    generated.append("def "+name+"("+params+"): # do not edit this line.");
    generated.append(delims + "# Automatically generated code. Do not edit manually.");
    generated.append(delims + "# Generated "+time.strftime("%c"))
    generated.extend([delims + x for x in head])
    generated.append(delims + "# Begin of manually editable code section. It is safe to edit below.");
    generated.extend(mid_part)
    generated.append(delims + "# End of manually editable code section. It is NOT safe to edit below.");
    generated.extend([delims + x for x in tail])
    generated.append(delims + "# End of automatically generated code section. Do not edit manually.");

    for i in range(starts,ends):
        contents.pop(starts)

    for i in range(len(generated)):
        contents.insert(starts+i,generated[i])
    if len(contents) > starts+len(generated):
        if contents[starts+len(generated)] != "":
            contents.insert(starts+len(generated),"")

def PY_import(contents, module):
    for x in contents:
        if delim_spacer(x).startswith("import "+module):
            return
    contents.insert(3,"import "+module)

def PY_alloc(contents, struct):
    name = struct["STRUCT"]+"_alloc"
    params = ""
    head = []
    head.append("")
    head.append("x = {}")
    head.append("")

    for (t0,t1),F in zip(struct["TYPES"],struct["NAMES"]):
        if t0 == "":
            initializer = PY_types[t1]
        elif t0 == "STRING":
            initializer = "\"\""
        elif t0 == "ARRAY":
            initializer = PY_arrays[t1]
        elif t0 == "STRUCT":
            initializer = "{}"
        elif t0.startswith("["):
            initializer = PY_arrays[t1]
        if t0 != "":
            t0 += " "
        head.append(fill_up("x['"+F+"'] = "+initializer,46)+"# "+t0+t1)
        if t0.startswith("["):
            head.append("for idx in range("+t0[1:-2]+"):")
            if t1 == "CHAR":
                head.append("    x['"+F+"'] += "+ PY_types[t1]+"")
            else:
                head.append("    x['"+F+"'].append("+ PY_types[t1]+")")


    tail = ["return x"]
    PY_def(contents,name,params,head,tail)

def PY_fix(contents, struct):
    name = struct["STRUCT"]+"_fix"
    params = "y"
    head = []
    head.append("")
    head.append("x = "+struct["STRUCT"]+"_alloc()")
    head.append("")

    for (t0,t1),F,opts in zip(struct["TYPES"],struct["NAMES"],struct["OPTIONS"]):
        if t0 == "":
            initializer = "= "+PY_converts[t1]+"(y['"+F+"'])"
        elif t0 == "STRING":
            initializer = "= str(y['"+F+"']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')"
        elif t0 == "ARRAY":
            if t1 == "CHAR":
                initializer = "= str(y['"+F+"'])"
            else:
                initializer = ".extend(["+PY_converts[t1]+"(item) for item in y['"+F+"']])"
        elif t0 == "STRUCT":
            initializer = "= "+t1+"_fix(y['"+F+"'])"
        if t0.startswith("["):
            if t1 == "CHAR":
                head.append("no_u = " + PY_converts[t1]+"(y['"+F
                             +"']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')")
                if "CSAFE" in opts:
                    head.append("x['"+F+"'] = no_u[:"+str(int(t0[1:-1])-1)+"]")
                else:
                    head.append("x['"+F+"'] = no_u[:"+t0[1:-1]+"]")
                head.append("if len(x['"+F+"'])<"+t0[1:-1]+":")
                head.append("    x['"+F+"'] += \"\\x00\"*("+t0[1:-1]+"-len(x['"+F+"']))")
            else:
                if "CSAFE" in opts:
                    head.append("for idx in range("+str(int(t0[1:-1])-1)+"):")
                else:
                    head.append("for idx in range("+t0[1:-1]+"):")
                head.append("    if len(y['"+F+"'])<=idx:")
                head.append("        x['"+F+"'][idx] = " + PY_types[t1])
                head.append("    else:")
                head.append("        x['"+F+"'][idx] = " + PY_converts[t1]+"(y['"+F+"'][idx])")
                # ..._alloc initializes the arrays with zeros -> no need to do it twice :)
        else:
            head.append(fill_up("x['"+F+"']"+initializer,46)+"# "+t0+t1)

    tail = ["return x"]
    PY_def(contents,name,params,head,tail)

def PY_read(contents, struct):
    name = struct["STRUCT"]+"_read"
    params = "f"
    head = []
    head.append("")
    head.append("x = "+struct["STRUCT"]+"_alloc()")
    head.append("")

    if not "UNSAFE_IO" in struct:
        info = IO_coding(struct).encode(encoding="utf-8")
        head.append("info = "+repr(info))
        head.append("check = bytes(f.read("+str(len(info))+"))")
        head.append("if info != check:")
        head.append("    return None")

    for (t0,t1),F,opts in zip(struct["TYPES"],struct["NAMES"],struct["OPTIONS"]):
        if "NOI/O" in opts:
            continue
        if t0 == "":
            head.append("data = bytes(f.read("+str(sizeof[t1])+"))")
            if t1 == "CHAR":
                head.append("x['"+F+"'] = data.decode(encoding='cp850')")
            else:
                head.append("x['"+F+"'] = struct.Struct("+repr(PY_struct_codes[t1])+").unpack(data)[0]")
        elif t0 == "STRING":
            if "CI/O" in opts:
                head.append("data0 = bytearray()")
                head.append("data = bytes(f.read(1))")
                head.append("while data:")
                head.append("    if data[0] == 0:")
                head.append("        break")
                head.append("    data0.append(data[0])")
                head.append("    data = bytes(f.read(1))")
                head.append("x['"+F+"'] = data0.decode(encoding='cp850')")
            else:
                head.append("strlen_d = bytes(f.read("+str(sizeof["INT32"])+"))")
                head.append("strlen = struct.Struct("+repr(PY_struct_codes["INT32"])+").unpack(strlen_d)[0]")
                head.append("data = bytes(f.read(strlen))")
                head.append("x['"+F+"'] = data.decode(encoding='cp850')")
        elif t0 == "ARRAY":
            X = PY_arrays[t1]
            if X.startswith("array.array"):
                head.append("N_d = bytes(f.read("+str(sizeof["INT32"])+"))")
                head.append("N = struct.Struct("+repr(PY_struct_codes["INT32"])+").unpack(N_d)[0]")
                head.append("data = bytes(f.read(N*"+str(sizeof[t1])+"))")
                head.append("if data:")
                head.append("    x['"+F+"'] = " + X)
                head.append("    x['"+F+"'].frombytes(data)")
            elif t1 == "CHAR":
                head.append("strlen_d = bytes(f.read("+str(sizeof["INT32"])+"))")
                head.append("strlen = struct.Struct("+repr(PY_struct_codes["INT32"])+").unpack(strlen_d)[0]")
                head.append("data = bytes(f.read(strlen))")
                head.append("x['"+F+"'] = data.decode(encoding='cp850')")
            else:
                head.append("N_d = bytes(f.read("+str(sizeof["INT32"])+"))")
                head.append("N = struct.Struct("+repr(PY_struct_codes["INT32"])+").unpack(N_d)[0]")
                head.append("data = bytes(f.read(N*"+str(sizeof[t1])+"))")
                head.append("cvtr = struct.Struct("+repr(PY_struct_codes[t1])+")")
                head.append("x['"+F+"'] = [cvtr.unpack(data[i:i+"+str(sizeof[t1])+
                                           "])[0] for i in range(0,N*"+str(sizeof[t1])+
                                            ","+str(sizeof[t1])+")]")
        elif t0.startswith("["):
            X = PY_arrays[t1]
            if X.startswith("array.array"):
                head.append("N = "+t0[1:-1])
                head.append("data = bytes(f.read(N*"+str(sizeof[t1])+"))")
                head.append("if data:")
                head.append("    x['"+F+"'] = " + X)
                head.append("    x['"+F+"'].frombytes(data)")
            elif t1 == "CHAR":
                head.append("strlen = "+t0[1:-1])
                head.append("data = bytes(f.read(strlen))")
                head.append("x['"+F+"'] = data.decode(encoding='cp850')")
            else:
                head.append("N = "+t0[1:-1])
                head.append("data = bytes(f.read(N*"+str(sizeof[t1])+"))")
                head.append("cvtr = struct.Struct("+repr(PY_struct_codes[t1])+")")
                head.append("x['"+F+"'] = [cvtr.unpack(data[i:i+"+str(sizeof[t1])+
                                           "])[0] for i in range(0,N*"+str(sizeof[t1])+
                                            ","+str(sizeof[t1])+")]")
        elif t0 == "STRUCT":
            head.append("x['"+F+"'] = "+t1+"_read(f)")

    tail = ["return x"]
    PY_def(contents,name,params,head,tail)

def PY_write(contents, struct):
    name = struct["STRUCT"]+"_write"
    params = "x, f"
    head = []

    head.append("x = "+struct["STRUCT"]+"_fix(x)")

    if not "UNSAFE_IO" in struct:
        info = IO_coding(struct).encode(encoding="utf-8")
        head.append("info = "+repr(info))
        head.append("f.write(info)")

    for (t0,t1),F,opts in zip(struct["TYPES"],struct["NAMES"],struct["OPTIONS"]):
        if "NOI/O" in opts:
            continue
        if t0 == "":
            if t1 == "CHAR":
                head.append("f.write(x['"+F+"'].encode(encoding='utf-8')[0:1])")
            else:
                head.append("f.write(struct.Struct("+repr(PY_struct_codes[t1])+").pack(x['"+F+"']))")
        elif t0 == "STRING":
            head.append("data = x['"+F+"'].encode(encoding='utf-8')")
            if "CI/O" in opts:
                head.append("data0 = bytearray()")
                head.append("for c in data:")
                head.append("    if c == 0:")
                head.append("        break")
                head.append("    data0.append(c)")
                head.append("data0.append(0)")
                head.append("f.write(bytes(data0))")
            else:
                head.append("strlen = len(data)")
                head.append("f.write(struct.Struct("+repr(PY_struct_codes["INT32"])+").pack(strlen))")
                head.append("f.write(data)")
        elif t0 == "ARRAY" or t0.startswith("["):
            X = PY_arrays[t1]
            if X.startswith("array.array"):
                head.append("N = len(x['"+F+"'])")
                head.append("f.write(struct.Struct("+repr(PY_struct_codes["INT32"])+").pack(N))")
                head.append("f.write(x['"+F+"'].tobytes())")
            elif t1 == "CHAR":
                head.append("data = x['"+F+"'].encode(encoding='utf-8')")
                if t0.startswith("["):
                    head.append("data = data[:"+t0[1:-1]+"]")
                head.append("strlen = len(data)")
                head.append("f.write(struct.Struct("+repr(PY_struct_codes["INT32"])+").pack(strlen))")
                head.append("f.write(data)")
            else:
                head.append("N = len(x['"+F+"'])")
                head.append("f.write(struct.Struct("+repr(PY_struct_codes["INT32"])+").pack(N))")
                head.append("cvtr = struct.Struct("+repr(PY_struct_codes[t1])+")")
                head.append("for item in x['"+F+"']:")
                head.append("    f.write(cvtr.pack(item))")
        elif t0 == "STRUCT":
            head.append(t1+"_write(x['"+F+"'],f)")

    tail = []
    PY_def(contents,name,params,head,tail)
def update_PY(filename, struct):
    contents_all = []
    if os.path.exists(filename+".py"):
        f = open(filename+".py", encoding="utf-8")
        contents_all = [kill_newline(x) for x in f.readlines()]
        f.close()

    mark = PY_mark(contents_all)
    contents = contents_all[:mark]
    bottom = contents_all[mark:]


    # the header is merely for convenience
    PY_header(contents)

    # import binary data python modules
    PY_import(contents,"array")
    PY_import(contents,"struct")

    # routines
    PY_alloc(contents,struct)
    PY_fix(contents,struct)
    PY_read(contents,struct)
    PY_write(contents,struct)

    # add the bottom of the script

    contents.extend(bottom)

    f = open(filename+".py","w",encoding="utf-8")
    for l in contents:
        f.write(l+"\n")
    f.close()
    

def do_updates(files, struct):
    c_list = files.get("C",{})
    for x in c_list:
        update_C(x, struct)
    py_list = files.get("PY",{})
    for x in py_list:
        update_PY(x, struct)
    


def update(filename):
    """updates the requested source files according to the file given by filename"""
    f = open(filename, encoding="utf-8")
    desc = [delim_spacer(x) for x in f.readlines()]
    desc = [x for x in desc if not x.startswith("#") and not x == ""] # kill comments.
    DESC = [x.upper() for x in desc]
    dzip = [x for x in zip(desc,DESC)]
    f.close()

    output_files = {}
    for x,X in dzip:
        if X.startswith("C "):
            c_list = output_files.get("C",{})
            c_name = strip_C(x.split(" ")[1])
            c_list[c_name] = c_name
            output_files["C"] = c_list
            print("Output C: ",c_name,".c/h")
        elif X.startswith("PYTHON "):
            py_list = output_files.get("PY",{})
            py_name = strip_PY(x.split(" ")[1])
            py_list[py_name] = py_name
            output_files["PY"] = py_list
            print("Output Python: ",py_name,".py")

    struct = new_struct(os.path.basename(filename))

    for x,X in dzip:
        if X.startswith("NAME "):
            struct = new_struct(x.split(" ")[1])
        elif X.startswith("END "):
            if struct["STRUCT"] != x.split(" ")[1]:
                print("Error: END ",x.split(" ")[1]," given, but END ",struct["STRUCT"]," expected!")
            else:
                print("Updating ",struct["STRUCT"])
                do_updates(output_files,struct)
        elif X.startswith("UNSAFE"):
            struct["UNSAFE_IO"] = 1
        else: # should be type declaration
            add_member(struct,x,X)
            
        

info = sys.argv[0] + """ creates C and Python code for given binary data structures

 Input file format
 =================

 The input files are plain text files, that contain line by line instructions.

 Comments
 --------

 If the first non-space character on a line is #, then this line is regarded
 to be a comment.

   >    #  This line is a comment



 Generating Output
 -----------------

 The following commands generate output

    C FILENAME
    C FILENAME.c
    C FILENAME.h

 These three commands all generate the same output to the files FILENAME.c
 and FILENAME.h, where FILENAME.h contains the data structure definitions
 and function declarations, and where FILENAME.c contains the implementati-
 ons of the declared generated functions.
 The files will be updated if they already exists, and previously generated
 code parts will be replaced if the files already contain generated code.

    PY FILENAME
    PY FILENAME.py

 These two commands both generate the same output to the file FILENAME.py.
 The file will be updated if it already exists, and previously generated code
 parts will be replaced if the files already contain generated code.

 Please note that it is possible to define any number of output files.


 Describing Data Structures
 --------------------------

 Each data structure is describe in a block that starts with
    
     NAME name_of_the_struct

 and that ends with

     END name_of_the_struct

 Optionally, you may specify the keyword

     UNSAFE

 in order to signal that the code generated for i/o should not write or check
 information about the structures fields.


 There are four types of data fields that may be specified, and every data
 field may be supplied with a list of additional options.

     {TYPE}             name_of_field  {{OPTIONS}}

  Declares a member of the structure with a fixed-size data type.

     [SIZE] {TYPE}      name_of_field  {{OPTIONS}}

  Declares a fixed-size-array member of the structure, whose elements have a
  fixed-size data type.

     ARRAY {TYPE}       name_of_field  {{OPTIONS}}

  Declares a member of the structure that is an array of a fixed-size data type.
  Arrays contain information about their length and their contents.

  The following fixed size data types are recognized: 
     """ + "\n     ".join(["%6s    interpreted as   %s"%(x,C_types[x]) for x in do_sort(C_types)]) + """
     
     STRING             name_of_field  {{OPTIONS}}

  Declares a member of the structure that is a string.

     STRUCT type_name   name_of_field  {{OPTIONS}}

  Declares a member of the structure that has the type type_name, which will
  be initialized with all zeros, and will be regarded as if it would be a poin-
  ter to another data structure generated by this tool.


  There are a number of options available, which can go in any order after the
  field's name.

     CI/O

  Signals that a string field is stored as a (very unsafe) C style string, i.e.
  it is stored without its size first, but instead zero-terminated. The maximum
  length of such a string in the C implementation is governed by MAX_CIO_SIZE.

     CSAFE

  Signals that the fixed-size array terminates in a zero. This is implemented
  by forcing the last array item to be zero regardless whether there are other
  array items that are zero before. Only applies to [SIZE] ... fields.

     NOALLOC

  Signals that the field shall not be allocated when the structure is alloced,
  instead, the field will be zero'd. Only applies to ARRAY and STRING. STRUCTS
  are always zero'd and never initialized by generated code and to the function
  name_of_the_structure_alloc().

     NOCMP

  Signals that the field is not to be used for the the generated comparison
  functions.

     NOFREE

  Signals that the fields contents shall not be freed, only applies to STRUCT,
  ARRAY and STRING type fields.

     NOI/O

  Signals that the field shall not be saved or restored by the generated file
  i/o routines.

  
  C Output
  --------

  The following C code will be generated:

   Types
   .....


     typedef struct t_name_of_the_struct {
              ...
     } s_name_of_the_struct;

     typedef s_name_of_the_struct *name_of_the_struct;


   Memory Management
   .................
     
     name_of_the_struct name_of_the_struct_alloc(...);

   Creates a new struct on the heap and fills it with zeros. For each array
   member, there is a parameter specifying the desired number of elements.

     void name_of_the_struct_free(name_of_the_struct x);

   Frees a struct from the heap, also frees the allocated arrays that belong
   to the struct.


   File I/O
   ........

     name_of_the_struct name_of_the_struct_alloc_from_file(FILE *f);

   Creates a new struct on the heap from the contents of the file f, checks
   whether the file indeed contains a compatible structure unless UNSAFE was
   specified. If the file is incompatible, this routine returns zero.

     void name_of_the_struct_write_to_file(name_of_the_struct x, FILE *f);

   Writes the contents of the structure x to the file f. Unless UNSAFE is spe-
   cified, includes information about the structure's fields first.


   Convenience
   ...........

     int name_of_the_struct_cmp(name_of_the_struct l, name_of_the_struct r);

   Compares l and r, returns -1 if l is smaller, 1 if r is smaller, and 0 if
   l and r are equal.

 
  Python Output
  -------------

  The following Python code will be generated:


    def name_of_the_struct_alloc(): 
            ...

  Creates a new dictionary object and initializes the member fields according
  to the structure definition with default values.


    def name_of_the_struct_fix(x):
            ...
  
  Fixes the contents of a dictionary x to meet the type requirements for the
  data structure.


    def name_of_the_struct_read(f):
            ...

  Creates a new dictionary object and fills its member fields with the contents
  of the file object f.

  Usage:
    > with open("structure.dat","rb") as f:
    >     x = name_of_the_struct_read(f)


    def name_of_the_struct_write(x, f):
            ...

  Writes the structure from the dictionary x to the file object f.
  
"""


if len(sys.argv) < 2:
    print("""Usage: %s file1 [file2 ...]
    Generates/updates the appropriate code files according to the data
    structure descriptions found in the input files.

%s --help
    print help on input data format    
    """%(sys.argv[0],sys.argv[0]))
elif sys.argv[1] == "--help" and len(sys.argv)==2:
    print(info)
else:
    for p in sys.argv[1:]:
        update(p)
