#!/usr/bin/python3 
# coding: utf-8
#
#  This file is a demonstration for datastructures.py
#
#

import struct
import array
import sys,os

def impulse_header_alloc(): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = {}
    
    x['IMPM_mark'] = ""                           # [4] CHAR
    for idx in range(4):
        x['IMPM_mark'] += chr(0)
    x['SongName'] = ""                            # [26] CHAR
    for idx in range(26):
        x['SongName'] += chr(0)
    x['PHiligt'] = 0                              # UINT16
    x['OrdNum'] = 0                               # UINT16
    x['InsNum'] = 0                               # UINT16
    x['SmpNum'] = 0                               # UINT16
    x['PatNum'] = 0                               # UINT16
    x['CwtV'] = 0                                 # UINT16
    x['Cmwt'] = 0                                 # UINT16
    x['Flags'] = 0                                # UINT16
    x['Special'] = 0                              # UINT16
    x['GV'] = 0                                   # UINT8
    x['MV'] = 0                                   # UINT8
    x['IS'] = 0                                   # UINT8
    x['IT'] = 0                                   # UINT8
    x['Sep'] = 0                                  # UINT8
    x['PWD'] = 0                                  # UINT8
    x['MsgLgth'] = 0                              # UINT16
    x['MsgOffs'] = 0                              # UINT32
    x['Reserved'] = 0                             # UINT32
    x['ChnlPan'] = array.array('b')               # [64] INT8
    for idx in range(64):
        x['ChnlPan'].append(0)
    x['ChnlVol'] = array.array('b')               # [64] INT8
    for idx in range(64):
        x['ChnlVol'].append(0)
    # Begin of manually editable code section. It is safe to edit below.
    
    x['Orders'] = array.array('B')
    x['OffsetInstruments'] = array.array('I')
    x['OffsetSamples'] = array.array('I')
    x['OffsetPatterns'] = array.array('I')
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_header_fix(y): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = impulse_header_alloc()
    
    no_u = str(y['IMPM_mark']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['IMPM_mark'] = no_u[:4]
    if len(x['IMPM_mark'])<4:
        x['IMPM_mark'] += "\x00"*(4-len(x['IMPM_mark']))
    no_u = str(y['SongName']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['SongName'] = no_u[:25]
    if len(x['SongName'])<26:
        x['SongName'] += "\x00"*(26-len(x['SongName']))
    x['PHiligt']= int(y['PHiligt'])               # UINT16
    x['OrdNum']= int(y['OrdNum'])                 # UINT16
    x['InsNum']= int(y['InsNum'])                 # UINT16
    x['SmpNum']= int(y['SmpNum'])                 # UINT16
    x['PatNum']= int(y['PatNum'])                 # UINT16
    x['CwtV']= int(y['CwtV'])                     # UINT16
    x['Cmwt']= int(y['Cmwt'])                     # UINT16
    x['Flags']= int(y['Flags'])                   # UINT16
    x['Special']= int(y['Special'])               # UINT16
    x['GV']= int(y['GV'])                         # UINT8
    x['MV']= int(y['MV'])                         # UINT8
    x['IS']= int(y['IS'])                         # UINT8
    x['IT']= int(y['IT'])                         # UINT8
    x['Sep']= int(y['Sep'])                       # UINT8
    x['PWD']= int(y['PWD'])                       # UINT8
    x['MsgLgth']= int(y['MsgLgth'])               # UINT16
    x['MsgOffs']= int(y['MsgOffs'])               # UINT32
    x['Reserved']= int(y['Reserved'])             # UINT32
    for idx in range(64):
        if len(y['ChnlPan'])<=idx:
            x['ChnlPan'][idx] = 0
        else:
            x['ChnlPan'][idx] = int(y['ChnlPan'][idx])
    for idx in range(64):
        if len(y['ChnlVol'])<=idx:
            x['ChnlVol'][idx] = 0
        else:
            x['ChnlVol'][idx] = int(y['ChnlVol'][idx])
    # Begin of manually editable code section. It is safe to edit below.

    x['OrdNum'] = len(x['Orders'])
    x['InsNum'] = len(x['OffsetInstruments'])
    x['PatNum'] = len(x['OffsetPatterns'])
    x['SmpNum'] = len(x['OffsetSamples'])
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_header_read(f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = impulse_header_alloc()
    
    strlen = 4
    data = bytes(f.read(strlen))
    x['IMPM_mark'] = data.decode(encoding='cp850')
    strlen = 26
    data = bytes(f.read(strlen))
    x['SongName'] = data.decode(encoding='cp850')
    data = bytes(f.read(2))
    x['PHiligt'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['OrdNum'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['InsNum'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['SmpNum'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['PatNum'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['CwtV'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['Cmwt'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['Flags'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['Special'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(1))
    x['GV'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['MV'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['IS'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['IT'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['Sep'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['PWD'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(2))
    x['MsgLgth'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(4))
    x['MsgOffs'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(4))
    x['Reserved'] = struct.Struct('=L').unpack(data)[0]
    N = 64
    data = bytes(f.read(N*1))
    if data:
        x['ChnlPan'] = array.array('b')
        x['ChnlPan'].frombytes(data)
    N = 64
    data = bytes(f.read(N*1))
    if data:
        x['ChnlVol'] = array.array('b')
        x['ChnlVol'].frombytes(data)
    # Begin of manually editable code section. It is safe to edit below.

    data = bytes(f.read(x['OrdNum']))
    if data:
        x['Orders'].frombytes(data)

    data = bytes(f.read(x['InsNum']*4))
    if data:
        x['OffsetInstruments'].frombytes(data)
    data = bytes(f.read(x['SmpNum']*4))
    if data:
        x['OffsetSamples'].frombytes(data)
    data = bytes(f.read(x['PatNum']*4))
    if data:
        x['OffsetPatterns'].frombytes(data)
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_header_write(x, f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    x = impulse_header_fix(x)
    data = x['IMPM_mark'].encode(encoding='utf-8')
    data = data[:4]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    data = x['SongName'].encode(encoding='utf-8')
    data = data[:26]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    f.write(struct.Struct('=H').pack(x['PHiligt']))
    f.write(struct.Struct('=H').pack(x['OrdNum']))
    f.write(struct.Struct('=H').pack(x['InsNum']))
    f.write(struct.Struct('=H').pack(x['SmpNum']))
    f.write(struct.Struct('=H').pack(x['PatNum']))
    f.write(struct.Struct('=H').pack(x['CwtV']))
    f.write(struct.Struct('=H').pack(x['Cmwt']))
    f.write(struct.Struct('=H').pack(x['Flags']))
    f.write(struct.Struct('=H').pack(x['Special']))
    f.write(struct.Struct('=B').pack(x['GV']))
    f.write(struct.Struct('=B').pack(x['MV']))
    f.write(struct.Struct('=B').pack(x['IS']))
    f.write(struct.Struct('=B').pack(x['IT']))
    f.write(struct.Struct('=B').pack(x['Sep']))
    f.write(struct.Struct('=B').pack(x['PWD']))
    f.write(struct.Struct('=H').pack(x['MsgLgth']))
    f.write(struct.Struct('=L').pack(x['MsgOffs']))
    f.write(struct.Struct('=L').pack(x['Reserved']))
    N = len(x['ChnlPan'])
    f.write(struct.Struct('=l').pack(N))
    f.write(x['ChnlPan'].tobytes())
    N = len(x['ChnlVol'])
    f.write(struct.Struct('=l').pack(N))
    f.write(x['ChnlVol'].tobytes())
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    # End of automatically generated code section. Do not edit manually.


def impulse_instrument_alloc(): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = {}
    
    x['IMPI_mark'] = ""                           # [4] CHAR
    for idx in range(4):
        x['IMPI_mark'] += chr(0)
    x['Dos_FileName'] = ""                        # [13] CHAR
    for idx in range(13):
        x['Dos_FileName'] += chr(0)
    x['NNA'] = 0                                  # UINT8
    x['DCT'] = 0                                  # UINT8
    x['DCA'] = 0                                  # UINT8
    x['FadeOut'] = 0                              # UINT16
    x['PPS'] = 0                                  # UINT8
    x['PPC'] = 0                                  # UINT8
    x['GbV'] = 0                                  # UINT8
    x['DfP'] = 0                                  # UINT8
    x['RV'] = 0                                   # UINT8
    x['RP'] = 0                                   # UINT8
    x['TrkVers'] = 0                              # UINT16
    x['NoS'] = 0                                  # UINT8
    x['reserved'] = 0                             # UINT8
    x['InstrumentName'] = ""                      # [26] CHAR
    for idx in range(26):
        x['InstrumentName'] += chr(0)
    x['IFC'] = 0                                  # UINT8
    x['IFR'] = 0                                  # UINT8
    x['MCh'] = 0                                  # UINT8
    x['MPr'] = 0                                  # UINT8
    x['MidiBank'] = 0                             # UINT16
    x['Note_Sample_Table'] = array.array('B')     # [240] UINT8
    for idx in range(240):
        x['Note_Sample_Table'].append(0)
    x['VolEnv'] = {}                              # STRUCT envelope
    x['PanEnv'] = {}                              # STRUCT envelope
    x['PitchEnv'] = {}                            # STRUCT envelope
    x['wastedBytes'] = ""                         # [7] CHAR
    for idx in range(7):
        x['wastedBytes'] += chr(0)
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_instrument_fix(y): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = impulse_instrument_alloc()
    
    no_u = str(y['IMPI_mark']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['IMPI_mark'] = no_u[:4]
    if len(x['IMPI_mark'])<4:
        x['IMPI_mark'] += "\x00"*(4-len(x['IMPI_mark']))
    no_u = str(y['Dos_FileName']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['Dos_FileName'] = no_u[:12]
    if len(x['Dos_FileName'])<13:
        x['Dos_FileName'] += "\x00"*(13-len(x['Dos_FileName']))
    x['NNA']= int(y['NNA'])                       # UINT8
    x['DCT']= int(y['DCT'])                       # UINT8
    x['DCA']= int(y['DCA'])                       # UINT8
    x['FadeOut']= int(y['FadeOut'])               # UINT16
    x['PPS']= int(y['PPS'])                       # UINT8
    x['PPC']= int(y['PPC'])                       # UINT8
    x['GbV']= int(y['GbV'])                       # UINT8
    x['DfP']= int(y['DfP'])                       # UINT8
    x['RV']= int(y['RV'])                         # UINT8
    x['RP']= int(y['RP'])                         # UINT8
    x['TrkVers']= int(y['TrkVers'])               # UINT16
    x['NoS']= int(y['NoS'])                       # UINT8
    x['reserved']= int(y['reserved'])             # UINT8
    no_u = str(y['InstrumentName']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['InstrumentName'] = no_u[:25]
    if len(x['InstrumentName'])<26:
        x['InstrumentName'] += "\x00"*(26-len(x['InstrumentName']))
    x['IFC']= int(y['IFC'])                       # UINT8
    x['IFR']= int(y['IFR'])                       # UINT8
    x['MCh']= int(y['MCh'])                       # UINT8
    x['MPr']= int(y['MPr'])                       # UINT8
    x['MidiBank']= int(y['MidiBank'])             # UINT16
    for idx in range(240):
        if len(y['Note_Sample_Table'])<=idx:
            x['Note_Sample_Table'][idx] = 0
        else:
            x['Note_Sample_Table'][idx] = int(y['Note_Sample_Table'][idx])
    x['VolEnv']= envelope_fix(y['VolEnv'])        # STRUCTenvelope
    x['PanEnv']= envelope_fix(y['PanEnv'])        # STRUCTenvelope
    x['PitchEnv']= envelope_fix(y['PitchEnv'])    # STRUCTenvelope
    no_u = str(y['wastedBytes']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['wastedBytes'] = no_u[:7]
    if len(x['wastedBytes'])<7:
        x['wastedBytes'] += "\x00"*(7-len(x['wastedBytes']))
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_instrument_read(f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = impulse_instrument_alloc()
    
    strlen = 4
    data = bytes(f.read(strlen))
    x['IMPI_mark'] = data.decode(encoding='cp850')
    strlen = 13
    data = bytes(f.read(strlen))
    x['Dos_FileName'] = data.decode(encoding='cp850')
    data = bytes(f.read(1))
    x['NNA'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['DCT'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['DCA'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(2))
    x['FadeOut'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(1))
    x['PPS'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['PPC'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['GbV'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['DfP'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['RV'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['RP'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(2))
    x['TrkVers'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(1))
    x['NoS'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['reserved'] = struct.Struct('=B').unpack(data)[0]
    strlen = 26
    data = bytes(f.read(strlen))
    x['InstrumentName'] = data.decode(encoding='cp850')
    data = bytes(f.read(1))
    x['IFC'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['IFR'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['MCh'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['MPr'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(2))
    x['MidiBank'] = struct.Struct('=H').unpack(data)[0]
    N = 240
    data = bytes(f.read(N*1))
    if data:
        x['Note_Sample_Table'] = array.array('B')
        x['Note_Sample_Table'].frombytes(data)
    x['VolEnv'] = envelope_read(f)
    x['PanEnv'] = envelope_read(f)
    x['PitchEnv'] = envelope_read(f)
    strlen = 7
    data = bytes(f.read(strlen))
    x['wastedBytes'] = data.decode(encoding='cp850')
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_instrument_write(x, f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    x = impulse_instrument_fix(x)
    data = x['IMPI_mark'].encode(encoding='utf-8')
    data = data[:4]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    data = x['Dos_FileName'].encode(encoding='utf-8')
    data = data[:13]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    f.write(struct.Struct('=B').pack(x['NNA']))
    f.write(struct.Struct('=B').pack(x['DCT']))
    f.write(struct.Struct('=B').pack(x['DCA']))
    f.write(struct.Struct('=H').pack(x['FadeOut']))
    f.write(struct.Struct('=B').pack(x['PPS']))
    f.write(struct.Struct('=B').pack(x['PPC']))
    f.write(struct.Struct('=B').pack(x['GbV']))
    f.write(struct.Struct('=B').pack(x['DfP']))
    f.write(struct.Struct('=B').pack(x['RV']))
    f.write(struct.Struct('=B').pack(x['RP']))
    f.write(struct.Struct('=H').pack(x['TrkVers']))
    f.write(struct.Struct('=B').pack(x['NoS']))
    f.write(struct.Struct('=B').pack(x['reserved']))
    data = x['InstrumentName'].encode(encoding='utf-8')
    data = data[:26]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    f.write(struct.Struct('=B').pack(x['IFC']))
    f.write(struct.Struct('=B').pack(x['IFR']))
    f.write(struct.Struct('=B').pack(x['MCh']))
    f.write(struct.Struct('=B').pack(x['MPr']))
    f.write(struct.Struct('=H').pack(x['MidiBank']))
    N = len(x['Note_Sample_Table'])
    f.write(struct.Struct('=l').pack(N))
    f.write(x['Note_Sample_Table'].tobytes())
    envelope_write(x['VolEnv'],f)
    envelope_write(x['PanEnv'],f)
    envelope_write(x['PitchEnv'],f)
    data = x['wastedBytes'].encode(encoding='utf-8')
    data = data[:7]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    # End of automatically generated code section. Do not edit manually.


def envelope_alloc(): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = {}
    
    x['Flg'] = 0                                  # UINT8
    x['Num'] = 0                                  # UINT8
    x['LpB'] = 0                                  # UINT8
    x['LpE'] = 0                                  # UINT8
    x['SLB'] = 0                                  # UINT8
    x['SLE'] = 0                                  # UINT8
    x['NodePoints'] = array.array('B')            # [25] UINT8
    for idx in range(25):
        x['NodePoints'].append(0)
    x['reserved'] = 0                             # UINT8
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def envelope_fix(y): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = envelope_alloc()
    
    x['Flg']= int(y['Flg'])                       # UINT8
    x['Num']= int(y['Num'])                       # UINT8
    x['LpB']= int(y['LpB'])                       # UINT8
    x['LpE']= int(y['LpE'])                       # UINT8
    x['SLB']= int(y['SLB'])                       # UINT8
    x['SLE']= int(y['SLE'])                       # UINT8
    for idx in range(25):
        if len(y['NodePoints'])<=idx:
            x['NodePoints'][idx] = 0
        else:
            x['NodePoints'][idx] = int(y['NodePoints'][idx])
    x['reserved']= int(y['reserved'])             # UINT8
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def envelope_read(f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = envelope_alloc()
    
    data = bytes(f.read(1))
    x['Flg'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['Num'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['LpB'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['LpE'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['SLB'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['SLE'] = struct.Struct('=B').unpack(data)[0]
    N = 25
    data = bytes(f.read(N*1))
    if data:
        x['NodePoints'] = array.array('B')
        x['NodePoints'].frombytes(data)
    data = bytes(f.read(1))
    x['reserved'] = struct.Struct('=B').unpack(data)[0]
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def envelope_write(x, f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    x = envelope_fix(x)
    f.write(struct.Struct('=B').pack(x['Flg']))
    f.write(struct.Struct('=B').pack(x['Num']))
    f.write(struct.Struct('=B').pack(x['LpB']))
    f.write(struct.Struct('=B').pack(x['LpE']))
    f.write(struct.Struct('=B').pack(x['SLB']))
    f.write(struct.Struct('=B').pack(x['SLE']))
    N = len(x['NodePoints'])
    f.write(struct.Struct('=l').pack(N))
    f.write(x['NodePoints'].tobytes())
    f.write(struct.Struct('=B').pack(x['reserved']))
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    # End of automatically generated code section. Do not edit manually.


def impulse_sample_alloc(): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = {}
    
    x['IMPS_mark'] = ""                           # [4] CHAR
    for idx in range(4):
        x['IMPS_mark'] += chr(0)
    x['Dos_FileName'] = ""                        # [13] CHAR
    for idx in range(13):
        x['Dos_FileName'] += chr(0)
    x['GvL'] = 0                                  # UINT8
    x['Flg'] = 0                                  # UINT8
    x['Vol'] = 0                                  # UINT8
    x['SampleName'] = ""                          # [26] CHAR
    for idx in range(26):
        x['SampleName'] += chr(0)
    x['Cvt'] = 0                                  # UINT8
    x['DfP'] = 0                                  # UINT8
    x['Length'] = 0                               # UINT32
    x['LoopBegin'] = 0                            # UINT32
    x['LoopEnd'] = 0                              # UINT32
    x['C5Speed'] = 0                              # UINT32
    x['SusLoopBegin'] = 0                         # UINT32
    x['SusLoopEnd'] = 0                           # UINT32
    x['SamplePointer'] = 0                        # UINT32
    x['ViS'] = 0                                  # UINT8
    x['ViD'] = 0                                  # UINT8
    x['ViR'] = 0                                  # UINT8
    x['ViT'] = 0                                  # UINT8
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_sample_fix(y): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = impulse_sample_alloc()
    
    no_u = str(y['IMPS_mark']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['IMPS_mark'] = no_u[:4]
    if len(x['IMPS_mark'])<4:
        x['IMPS_mark'] += "\x00"*(4-len(x['IMPS_mark']))
    no_u = str(y['Dos_FileName']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['Dos_FileName'] = no_u[:12]
    if len(x['Dos_FileName'])<13:
        x['Dos_FileName'] += "\x00"*(13-len(x['Dos_FileName']))
    x['GvL']= int(y['GvL'])                       # UINT8
    x['Flg']= int(y['Flg'])                       # UINT8
    x['Vol']= int(y['Vol'])                       # UINT8
    no_u = str(y['SampleName']).encode(encoding='cp850',errors='replace').decode(encoding='cp850')
    x['SampleName'] = no_u[:25]
    if len(x['SampleName'])<26:
        x['SampleName'] += "\x00"*(26-len(x['SampleName']))
    x['Cvt']= int(y['Cvt'])                       # UINT8
    x['DfP']= int(y['DfP'])                       # UINT8
    x['Length']= int(y['Length'])                 # UINT32
    x['LoopBegin']= int(y['LoopBegin'])           # UINT32
    x['LoopEnd']= int(y['LoopEnd'])               # UINT32
    x['C5Speed']= int(y['C5Speed'])               # UINT32
    x['SusLoopBegin']= int(y['SusLoopBegin'])     # UINT32
    x['SusLoopEnd']= int(y['SusLoopEnd'])         # UINT32
    x['SamplePointer']= int(y['SamplePointer'])   # UINT32
    x['ViS']= int(y['ViS'])                       # UINT8
    x['ViD']= int(y['ViD'])                       # UINT8
    x['ViR']= int(y['ViR'])                       # UINT8
    x['ViT']= int(y['ViT'])                       # UINT8
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_sample_read(f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = impulse_sample_alloc()
    
    strlen = 4
    data = bytes(f.read(strlen))
    x['IMPS_mark'] = data.decode(encoding='cp850')
    strlen = 13
    data = bytes(f.read(strlen))
    x['Dos_FileName'] = data.decode(encoding='cp850')
    data = bytes(f.read(1))
    x['GvL'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['Flg'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['Vol'] = struct.Struct('=B').unpack(data)[0]
    strlen = 26
    data = bytes(f.read(strlen))
    x['SampleName'] = data.decode(encoding='cp850')
    data = bytes(f.read(1))
    x['Cvt'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['DfP'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(4))
    x['Length'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(4))
    x['LoopBegin'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(4))
    x['LoopEnd'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(4))
    x['C5Speed'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(4))
    x['SusLoopBegin'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(4))
    x['SusLoopEnd'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(4))
    x['SamplePointer'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(1))
    x['ViS'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['ViD'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['ViR'] = struct.Struct('=B').unpack(data)[0]
    data = bytes(f.read(1))
    x['ViT'] = struct.Struct('=B').unpack(data)[0]
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_sample_write(x, f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    x = impulse_sample_fix(x)
    data = x['IMPS_mark'].encode(encoding='utf-8')
    data = data[:4]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    data = x['Dos_FileName'].encode(encoding='utf-8')
    data = data[:13]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    f.write(struct.Struct('=B').pack(x['GvL']))
    f.write(struct.Struct('=B').pack(x['Flg']))
    f.write(struct.Struct('=B').pack(x['Vol']))
    data = x['SampleName'].encode(encoding='utf-8')
    data = data[:26]
    strlen = len(data)
    f.write(struct.Struct('=l').pack(strlen))
    f.write(data)
    f.write(struct.Struct('=B').pack(x['Cvt']))
    f.write(struct.Struct('=B').pack(x['DfP']))
    f.write(struct.Struct('=L').pack(x['Length']))
    f.write(struct.Struct('=L').pack(x['LoopBegin']))
    f.write(struct.Struct('=L').pack(x['LoopEnd']))
    f.write(struct.Struct('=L').pack(x['C5Speed']))
    f.write(struct.Struct('=L').pack(x['SusLoopBegin']))
    f.write(struct.Struct('=L').pack(x['SusLoopEnd']))
    f.write(struct.Struct('=L').pack(x['SamplePointer']))
    f.write(struct.Struct('=B').pack(x['ViS']))
    f.write(struct.Struct('=B').pack(x['ViD']))
    f.write(struct.Struct('=B').pack(x['ViR']))
    f.write(struct.Struct('=B').pack(x['ViT']))
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    # End of automatically generated code section. Do not edit manually.


def cached_sample_alloc(): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = {}
    
    x['header'] = {}                              # STRUCT impulse_sample
    x['FileSize'] = 0                             # UINT32
    x['Date'] = 0                                 # UINT16
    x['Time'] = 0                                 # UINT16
    x['Fmt'] = 0                                  # UINT8
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def cached_sample_fix(y): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = cached_sample_alloc()
    
    x['header']= impulse_sample_fix(y['header'])  # STRUCTimpulse_sample
    x['FileSize']= int(y['FileSize'])             # UINT32
    x['Date']= int(y['Date'])                     # UINT16
    x['Time']= int(y['Time'])                     # UINT16
    x['Fmt']= int(y['Fmt'])                       # UINT8
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def cached_sample_read(f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = cached_sample_alloc()
    
    x['header'] = impulse_sample_read(f)
    data = bytes(f.read(4))
    x['FileSize'] = struct.Struct('=L').unpack(data)[0]
    data = bytes(f.read(2))
    x['Date'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['Time'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(1))
    x['Fmt'] = struct.Struct('=B').unpack(data)[0]
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def cached_sample_write(x, f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    x = cached_sample_fix(x)
    impulse_sample_write(x['header'],f)
    f.write(struct.Struct('=L').pack(x['FileSize']))
    f.write(struct.Struct('=H').pack(x['Date']))
    f.write(struct.Struct('=H').pack(x['Time']))
    f.write(struct.Struct('=B').pack(x['Fmt']))
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    # End of automatically generated code section. Do not edit manually.


def impulse_pattern_alloc(): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = {}
    
    x['Length'] = 0                               # UINT16
    x['Rows'] = 0                                 # UINT16
    x['reserved'] = 0                             # UINT32
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_pattern_fix(y): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = impulse_pattern_alloc()
    
    x['Length']= int(y['Length'])                 # UINT16
    x['Rows']= int(y['Rows'])                     # UINT16
    x['reserved']= int(y['reserved'])             # UINT32
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_pattern_read(f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    
    x = impulse_pattern_alloc()
    
    data = bytes(f.read(2))
    x['Length'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(2))
    x['Rows'] = struct.Struct('=H').unpack(data)[0]
    data = bytes(f.read(4))
    x['reserved'] = struct.Struct('=L').unpack(data)[0]
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    return x
    # End of automatically generated code section. Do not edit manually.


def impulse_pattern_write(x, f): # do not edit this line.
    # Automatically generated code. Do not edit manually.
    # Generated Sat Aug 16 18:21:58 2014
    x = impulse_pattern_fix(x)
    f.write(struct.Struct('=H').pack(x['Length']))
    f.write(struct.Struct('=H').pack(x['Rows']))
    f.write(struct.Struct('=L').pack(x['reserved']))
    # Begin of manually editable code section. It is safe to edit below.
    
    # End of manually editable code section. It is NOT safe to edit below.
    # End of automatically generated code section. Do not edit manually.

# All generated code will be placed above this mark.

if (sys.argv[-1].upper().endswith(".IT") or 
   sys.argv[-1].upper().endswith(".MOD")):
    print("Contents of ",sys.argv[-1])
    with open(sys.argv[-1],"rb") as f:
        it = impulse_header_read(f)
        print("Name:",it["SongName"])
        print("Order:",it["Orders"])
        for offset in it["OffsetInstruments"]:
            f.seek(offset)
            ins = impulse_instrument_read(f)
            print("Instrument (%x): "%offset, ins["InstrumentName"])
        for offset in it["OffsetSamples"]:
            f.seek(offset)
            smp_cache = cached_sample_read(f)
            smp = smp_cache["header"]
            print("Sample (%x): "%offset, smp["SampleName"],"Flags: %x"%smp["Flg"])
            if smp["Length"] != 0:
                ratio = (smp_cache["FileSize"]/smp["Length"])
            else:
                ratio = -1
            print("  File (%x): "%smp["SamplePointer"],"%.2f KiB"%(smp_cache["FileSize"]/1024.),
                    "%d frames"%smp["Length"], 
                    "Ratio:%.5f=%d/%d"%(ratio,smp_cache["FileSize"],smp["Length"]))
        for offset in it["OffsetPatterns"]:
            f.seek(offset)
            pat = impulse_pattern_read(f)
            print("Pattern (%x): Length"%offset, pat["Length"])

