#include "it_file.h"
#include <assert.h>
#include <stdlib.h>
#include <string.h>





impulse_header impulse_header_alloc()
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    impulse_header x = calloc(1, sizeof(s_impulse_header));
    assert(x);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void impulse_header_free(impulse_header x)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 


   /* End of automatically generated code. Manual editing below is safe. */

    free(x);
}


impulse_header impulse_header_alloc_from_file(FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    impulse_header x;

    x = calloc(1, sizeof(s_impulse_header));
    assert(x);

    fread(&x->IMPM_mark, sizeof(x->IMPM_mark), 1, f);

    fread(&x->SongName, sizeof(x->SongName), 1, f);
    x->SongName[25] = 0;

    fread(&x->PHiligt, sizeof(uint16_t), 1, f);

    fread(&x->OrdNum, sizeof(uint16_t), 1, f);

    fread(&x->InsNum, sizeof(uint16_t), 1, f);

    fread(&x->SmpNum, sizeof(uint16_t), 1, f);

    fread(&x->PatNum, sizeof(uint16_t), 1, f);

    fread(&x->CwtV, sizeof(uint16_t), 1, f);

    fread(&x->Cmwt, sizeof(uint16_t), 1, f);

    fread(&x->Flags, sizeof(uint16_t), 1, f);

    fread(&x->Special, sizeof(uint16_t), 1, f);

    fread(&x->GV, sizeof(uint8_t), 1, f);

    fread(&x->MV, sizeof(uint8_t), 1, f);

    fread(&x->IS, sizeof(uint8_t), 1, f);

    fread(&x->IT, sizeof(uint8_t), 1, f);

    fread(&x->Sep, sizeof(uint8_t), 1, f);

    fread(&x->PWD, sizeof(uint8_t), 1, f);

    fread(&x->MsgLgth, sizeof(uint16_t), 1, f);

    fread(&x->MsgOffs, sizeof(uint32_t), 1, f);

    fread(&x->Reserved, sizeof(uint32_t), 1, f);

    fread(&x->ChnlPan, sizeof(x->ChnlPan), 1, f);

    fread(&x->ChnlVol, sizeof(x->ChnlVol), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void impulse_header_write_to_file(impulse_header x, FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    assert(x);

    fwrite(&x->IMPM_mark, sizeof(x->IMPM_mark), 1, f);

    x->SongName[25] = 0;
    fwrite(&x->SongName, sizeof(x->SongName), 1, f);

    fwrite(&x->PHiligt, sizeof(uint16_t), 1, f);

    fwrite(&x->OrdNum, sizeof(uint16_t), 1, f);

    fwrite(&x->InsNum, sizeof(uint16_t), 1, f);

    fwrite(&x->SmpNum, sizeof(uint16_t), 1, f);

    fwrite(&x->PatNum, sizeof(uint16_t), 1, f);

    fwrite(&x->CwtV, sizeof(uint16_t), 1, f);

    fwrite(&x->Cmwt, sizeof(uint16_t), 1, f);

    fwrite(&x->Flags, sizeof(uint16_t), 1, f);

    fwrite(&x->Special, sizeof(uint16_t), 1, f);

    fwrite(&x->GV, sizeof(uint8_t), 1, f);

    fwrite(&x->MV, sizeof(uint8_t), 1, f);

    fwrite(&x->IS, sizeof(uint8_t), 1, f);

    fwrite(&x->IT, sizeof(uint8_t), 1, f);

    fwrite(&x->Sep, sizeof(uint8_t), 1, f);

    fwrite(&x->PWD, sizeof(uint8_t), 1, f);

    fwrite(&x->MsgLgth, sizeof(uint16_t), 1, f);

    fwrite(&x->MsgOffs, sizeof(uint32_t), 1, f);

    fwrite(&x->Reserved, sizeof(uint32_t), 1, f);

    fwrite(&x->ChnlPan, sizeof(x->ChnlPan), 1, f);

    fwrite(&x->ChnlVol, sizeof(x->ChnlVol), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

}


int impulse_header_cmp(impulse_header l, impulse_header r)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    int32_t i, N;

    if (r == l) return 0;
    if (l == 0) return -1;
    if (r == 0) return 1;

    N = sizeof(l->IMPM_mark)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->IMPM_mark[i] < r->IMPM_mark[i]) return -1;
        if (r->IMPM_mark[i] < l->IMPM_mark[i]) return 1;
    }

    N = sizeof(l->SongName)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->SongName[i] < r->SongName[i]) return -1;
        if (r->SongName[i] < l->SongName[i]) return 1;
    }

    if (l->PHiligt < r->PHiligt) return -1;
    if (r->PHiligt < l->PHiligt) return 1;

    if (l->OrdNum < r->OrdNum) return -1;
    if (r->OrdNum < l->OrdNum) return 1;

    if (l->InsNum < r->InsNum) return -1;
    if (r->InsNum < l->InsNum) return 1;

    if (l->SmpNum < r->SmpNum) return -1;
    if (r->SmpNum < l->SmpNum) return 1;

    if (l->PatNum < r->PatNum) return -1;
    if (r->PatNum < l->PatNum) return 1;

    if (l->CwtV < r->CwtV) return -1;
    if (r->CwtV < l->CwtV) return 1;

    if (l->Cmwt < r->Cmwt) return -1;
    if (r->Cmwt < l->Cmwt) return 1;

    if (l->Flags < r->Flags) return -1;
    if (r->Flags < l->Flags) return 1;

    if (l->Special < r->Special) return -1;
    if (r->Special < l->Special) return 1;

    if (l->GV < r->GV) return -1;
    if (r->GV < l->GV) return 1;

    if (l->MV < r->MV) return -1;
    if (r->MV < l->MV) return 1;

    if (l->IS < r->IS) return -1;
    if (r->IS < l->IS) return 1;

    if (l->IT < r->IT) return -1;
    if (r->IT < l->IT) return 1;

    if (l->Sep < r->Sep) return -1;
    if (r->Sep < l->Sep) return 1;

    if (l->PWD < r->PWD) return -1;
    if (r->PWD < l->PWD) return 1;

    if (l->MsgLgth < r->MsgLgth) return -1;
    if (r->MsgLgth < l->MsgLgth) return 1;

    if (l->MsgOffs < r->MsgOffs) return -1;
    if (r->MsgOffs < l->MsgOffs) return 1;

    if (l->Reserved < r->Reserved) return -1;
    if (r->Reserved < l->Reserved) return 1;

    N = sizeof(l->ChnlPan)/sizeof(int8_t);
    for (i = 0; i < N; ++i) {
        if (l->ChnlPan[i] < r->ChnlPan[i]) return -1;
        if (r->ChnlPan[i] < l->ChnlPan[i]) return 1;
    }

    N = sizeof(l->ChnlVol)/sizeof(int8_t);
    for (i = 0; i < N; ++i) {
        if (l->ChnlVol[i] < r->ChnlVol[i]) return -1;
        if (r->ChnlVol[i] < l->ChnlVol[i]) return 1;
    }


   /* End of automatically generated code. Manual editing below is safe. */

    return 0;
}


impulse_instrument impulse_instrument_alloc()
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    impulse_instrument x = calloc(1, sizeof(s_impulse_instrument));
    assert(x);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void impulse_instrument_free(impulse_instrument x)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    if (x->VolEnv) envelope_free(x->VolEnv);
    if (x->PanEnv) envelope_free(x->PanEnv);
    if (x->PitchEnv) envelope_free(x->PitchEnv);

   /* End of automatically generated code. Manual editing below is safe. */

    free(x);
}


impulse_instrument impulse_instrument_alloc_from_file(FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    impulse_instrument x;

    x = calloc(1, sizeof(s_impulse_instrument));
    assert(x);

    fread(&x->IMPI_mark, sizeof(x->IMPI_mark), 1, f);

    fread(&x->Dos_FileName, sizeof(x->Dos_FileName), 1, f);
    x->Dos_FileName[12] = 0;

    fread(&x->NNA, sizeof(uint8_t), 1, f);

    fread(&x->DCT, sizeof(uint8_t), 1, f);

    fread(&x->DCA, sizeof(uint8_t), 1, f);

    fread(&x->FadeOut, sizeof(uint16_t), 1, f);

    fread(&x->PPS, sizeof(uint8_t), 1, f);

    fread(&x->PPC, sizeof(uint8_t), 1, f);

    fread(&x->GbV, sizeof(uint8_t), 1, f);

    fread(&x->DfP, sizeof(uint8_t), 1, f);

    fread(&x->RV, sizeof(uint8_t), 1, f);

    fread(&x->RP, sizeof(uint8_t), 1, f);

    fread(&x->TrkVers, sizeof(uint16_t), 1, f);

    fread(&x->NoS, sizeof(uint8_t), 1, f);

    fread(&x->reserved, sizeof(uint8_t), 1, f);

    fread(&x->InstrumentName, sizeof(x->InstrumentName), 1, f);
    x->InstrumentName[25] = 0;

    fread(&x->IFC, sizeof(uint8_t), 1, f);

    fread(&x->IFR, sizeof(uint8_t), 1, f);

    fread(&x->MCh, sizeof(uint8_t), 1, f);

    fread(&x->MPr, sizeof(uint8_t), 1, f);

    fread(&x->MidiBank, sizeof(uint16_t), 1, f);

    fread(&x->Note_Sample_Table, sizeof(x->Note_Sample_Table), 1, f);

    x->VolEnv = envelope_alloc_from_file(f);

    x->PanEnv = envelope_alloc_from_file(f);

    x->PitchEnv = envelope_alloc_from_file(f);

    fread(&x->wastedBytes, sizeof(x->wastedBytes), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void impulse_instrument_write_to_file(impulse_instrument x, FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    assert(x);

    fwrite(&x->IMPI_mark, sizeof(x->IMPI_mark), 1, f);

    x->Dos_FileName[12] = 0;
    fwrite(&x->Dos_FileName, sizeof(x->Dos_FileName), 1, f);

    fwrite(&x->NNA, sizeof(uint8_t), 1, f);

    fwrite(&x->DCT, sizeof(uint8_t), 1, f);

    fwrite(&x->DCA, sizeof(uint8_t), 1, f);

    fwrite(&x->FadeOut, sizeof(uint16_t), 1, f);

    fwrite(&x->PPS, sizeof(uint8_t), 1, f);

    fwrite(&x->PPC, sizeof(uint8_t), 1, f);

    fwrite(&x->GbV, sizeof(uint8_t), 1, f);

    fwrite(&x->DfP, sizeof(uint8_t), 1, f);

    fwrite(&x->RV, sizeof(uint8_t), 1, f);

    fwrite(&x->RP, sizeof(uint8_t), 1, f);

    fwrite(&x->TrkVers, sizeof(uint16_t), 1, f);

    fwrite(&x->NoS, sizeof(uint8_t), 1, f);

    fwrite(&x->reserved, sizeof(uint8_t), 1, f);

    x->InstrumentName[25] = 0;
    fwrite(&x->InstrumentName, sizeof(x->InstrumentName), 1, f);

    fwrite(&x->IFC, sizeof(uint8_t), 1, f);

    fwrite(&x->IFR, sizeof(uint8_t), 1, f);

    fwrite(&x->MCh, sizeof(uint8_t), 1, f);

    fwrite(&x->MPr, sizeof(uint8_t), 1, f);

    fwrite(&x->MidiBank, sizeof(uint16_t), 1, f);

    fwrite(&x->Note_Sample_Table, sizeof(x->Note_Sample_Table), 1, f);

    assert(x->VolEnv);
    envelope_write_to_file(x->VolEnv,f);

    assert(x->PanEnv);
    envelope_write_to_file(x->PanEnv,f);

    assert(x->PitchEnv);
    envelope_write_to_file(x->PitchEnv,f);

    fwrite(&x->wastedBytes, sizeof(x->wastedBytes), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

}


int impulse_instrument_cmp(impulse_instrument l, impulse_instrument r)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    int cmp;

    int32_t i, N;

    if (r == l) return 0;
    if (l == 0) return -1;
    if (r == 0) return 1;

    N = sizeof(l->IMPI_mark)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->IMPI_mark[i] < r->IMPI_mark[i]) return -1;
        if (r->IMPI_mark[i] < l->IMPI_mark[i]) return 1;
    }

    N = sizeof(l->Dos_FileName)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->Dos_FileName[i] < r->Dos_FileName[i]) return -1;
        if (r->Dos_FileName[i] < l->Dos_FileName[i]) return 1;
    }

    if (l->NNA < r->NNA) return -1;
    if (r->NNA < l->NNA) return 1;

    if (l->DCT < r->DCT) return -1;
    if (r->DCT < l->DCT) return 1;

    if (l->DCA < r->DCA) return -1;
    if (r->DCA < l->DCA) return 1;

    if (l->FadeOut < r->FadeOut) return -1;
    if (r->FadeOut < l->FadeOut) return 1;

    if (l->PPS < r->PPS) return -1;
    if (r->PPS < l->PPS) return 1;

    if (l->PPC < r->PPC) return -1;
    if (r->PPC < l->PPC) return 1;

    if (l->GbV < r->GbV) return -1;
    if (r->GbV < l->GbV) return 1;

    if (l->DfP < r->DfP) return -1;
    if (r->DfP < l->DfP) return 1;

    if (l->RV < r->RV) return -1;
    if (r->RV < l->RV) return 1;

    if (l->RP < r->RP) return -1;
    if (r->RP < l->RP) return 1;

    if (l->TrkVers < r->TrkVers) return -1;
    if (r->TrkVers < l->TrkVers) return 1;

    if (l->NoS < r->NoS) return -1;
    if (r->NoS < l->NoS) return 1;

    if (l->reserved < r->reserved) return -1;
    if (r->reserved < l->reserved) return 1;

    N = sizeof(l->InstrumentName)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->InstrumentName[i] < r->InstrumentName[i]) return -1;
        if (r->InstrumentName[i] < l->InstrumentName[i]) return 1;
    }

    if (l->IFC < r->IFC) return -1;
    if (r->IFC < l->IFC) return 1;

    if (l->IFR < r->IFR) return -1;
    if (r->IFR < l->IFR) return 1;

    if (l->MCh < r->MCh) return -1;
    if (r->MCh < l->MCh) return 1;

    if (l->MPr < r->MPr) return -1;
    if (r->MPr < l->MPr) return 1;

    if (l->MidiBank < r->MidiBank) return -1;
    if (r->MidiBank < l->MidiBank) return 1;

    N = sizeof(l->Note_Sample_Table)/sizeof(uint8_t);
    for (i = 0; i < N; ++i) {
        if (l->Note_Sample_Table[i] < r->Note_Sample_Table[i]) return -1;
        if (r->Note_Sample_Table[i] < l->Note_Sample_Table[i]) return 1;
    }

    if (l->VolEnv == 0)
    {
        if (r->VolEnv != 0) return 1;
    } else if (r->VolEnv == 0) return -1;
    else {
        cmp = envelope_cmp(l->VolEnv, r->VolEnv);
        if (cmp != 0) return cmp;
    }

    if (l->PanEnv == 0)
    {
        if (r->PanEnv != 0) return 1;
    } else if (r->PanEnv == 0) return -1;
    else {
        cmp = envelope_cmp(l->PanEnv, r->PanEnv);
        if (cmp != 0) return cmp;
    }

    if (l->PitchEnv == 0)
    {
        if (r->PitchEnv != 0) return 1;
    } else if (r->PitchEnv == 0) return -1;
    else {
        cmp = envelope_cmp(l->PitchEnv, r->PitchEnv);
        if (cmp != 0) return cmp;
    }

    N = sizeof(l->wastedBytes)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->wastedBytes[i] < r->wastedBytes[i]) return -1;
        if (r->wastedBytes[i] < l->wastedBytes[i]) return 1;
    }


   /* End of automatically generated code. Manual editing below is safe. */

    return 0;
}


envelope envelope_alloc()
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    envelope x = calloc(1, sizeof(s_envelope));
    assert(x);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void envelope_free(envelope x)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 


   /* End of automatically generated code. Manual editing below is safe. */

    free(x);
}


envelope envelope_alloc_from_file(FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    envelope x;

    x = calloc(1, sizeof(s_envelope));
    assert(x);

    fread(&x->Flg, sizeof(uint8_t), 1, f);

    fread(&x->Num, sizeof(uint8_t), 1, f);

    fread(&x->LpB, sizeof(uint8_t), 1, f);

    fread(&x->LpE, sizeof(uint8_t), 1, f);

    fread(&x->SLB, sizeof(uint8_t), 1, f);

    fread(&x->SLE, sizeof(uint8_t), 1, f);

    fread(&x->NodePoints, sizeof(x->NodePoints), 1, f);

    fread(&x->reserved, sizeof(uint8_t), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void envelope_write_to_file(envelope x, FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    assert(x);

    fwrite(&x->Flg, sizeof(uint8_t), 1, f);

    fwrite(&x->Num, sizeof(uint8_t), 1, f);

    fwrite(&x->LpB, sizeof(uint8_t), 1, f);

    fwrite(&x->LpE, sizeof(uint8_t), 1, f);

    fwrite(&x->SLB, sizeof(uint8_t), 1, f);

    fwrite(&x->SLE, sizeof(uint8_t), 1, f);

    fwrite(&x->NodePoints, sizeof(x->NodePoints), 1, f);

    fwrite(&x->reserved, sizeof(uint8_t), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

}


int envelope_cmp(envelope l, envelope r)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    int32_t i, N;

    if (r == l) return 0;
    if (l == 0) return -1;
    if (r == 0) return 1;

    if (l->Flg < r->Flg) return -1;
    if (r->Flg < l->Flg) return 1;

    if (l->Num < r->Num) return -1;
    if (r->Num < l->Num) return 1;

    if (l->LpB < r->LpB) return -1;
    if (r->LpB < l->LpB) return 1;

    if (l->LpE < r->LpE) return -1;
    if (r->LpE < l->LpE) return 1;

    if (l->SLB < r->SLB) return -1;
    if (r->SLB < l->SLB) return 1;

    if (l->SLE < r->SLE) return -1;
    if (r->SLE < l->SLE) return 1;

    N = sizeof(l->NodePoints)/sizeof(uint8_t);
    for (i = 0; i < N; ++i) {
        if (l->NodePoints[i] < r->NodePoints[i]) return -1;
        if (r->NodePoints[i] < l->NodePoints[i]) return 1;
    }

    if (l->reserved < r->reserved) return -1;
    if (r->reserved < l->reserved) return 1;


   /* End of automatically generated code. Manual editing below is safe. */

    return 0;
}


impulse_sample impulse_sample_alloc()
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    impulse_sample x = calloc(1, sizeof(s_impulse_sample));
    assert(x);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void impulse_sample_free(impulse_sample x)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 


   /* End of automatically generated code. Manual editing below is safe. */

    free(x);
}


impulse_sample impulse_sample_alloc_from_file(FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    impulse_sample x;

    x = calloc(1, sizeof(s_impulse_sample));
    assert(x);

    fread(&x->IMPS_mark, sizeof(x->IMPS_mark), 1, f);

    fread(&x->Dos_FileName, sizeof(x->Dos_FileName), 1, f);
    x->Dos_FileName[12] = 0;

    fread(&x->GvL, sizeof(uint8_t), 1, f);

    fread(&x->Flg, sizeof(uint8_t), 1, f);

    fread(&x->Vol, sizeof(uint8_t), 1, f);

    fread(&x->SampleName, sizeof(x->SampleName), 1, f);
    x->SampleName[25] = 0;

    fread(&x->Cvt, sizeof(uint8_t), 1, f);

    fread(&x->DfP, sizeof(uint8_t), 1, f);

    fread(&x->Length, sizeof(uint32_t), 1, f);

    fread(&x->LoopBegin, sizeof(uint32_t), 1, f);

    fread(&x->LoopEnd, sizeof(uint32_t), 1, f);

    fread(&x->C5Speed, sizeof(uint32_t), 1, f);

    fread(&x->SusLoopBegin, sizeof(uint32_t), 1, f);

    fread(&x->SusLoopEnd, sizeof(uint32_t), 1, f);

    fread(&x->SamplePointer, sizeof(uint32_t), 1, f);

    fread(&x->ViS, sizeof(uint8_t), 1, f);

    fread(&x->ViD, sizeof(uint8_t), 1, f);

    fread(&x->ViR, sizeof(uint8_t), 1, f);

    fread(&x->ViT, sizeof(uint8_t), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void impulse_sample_write_to_file(impulse_sample x, FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    assert(x);

    fwrite(&x->IMPS_mark, sizeof(x->IMPS_mark), 1, f);

    x->Dos_FileName[12] = 0;
    fwrite(&x->Dos_FileName, sizeof(x->Dos_FileName), 1, f);

    fwrite(&x->GvL, sizeof(uint8_t), 1, f);

    fwrite(&x->Flg, sizeof(uint8_t), 1, f);

    fwrite(&x->Vol, sizeof(uint8_t), 1, f);

    x->SampleName[25] = 0;
    fwrite(&x->SampleName, sizeof(x->SampleName), 1, f);

    fwrite(&x->Cvt, sizeof(uint8_t), 1, f);

    fwrite(&x->DfP, sizeof(uint8_t), 1, f);

    fwrite(&x->Length, sizeof(uint32_t), 1, f);

    fwrite(&x->LoopBegin, sizeof(uint32_t), 1, f);

    fwrite(&x->LoopEnd, sizeof(uint32_t), 1, f);

    fwrite(&x->C5Speed, sizeof(uint32_t), 1, f);

    fwrite(&x->SusLoopBegin, sizeof(uint32_t), 1, f);

    fwrite(&x->SusLoopEnd, sizeof(uint32_t), 1, f);

    fwrite(&x->SamplePointer, sizeof(uint32_t), 1, f);

    fwrite(&x->ViS, sizeof(uint8_t), 1, f);

    fwrite(&x->ViD, sizeof(uint8_t), 1, f);

    fwrite(&x->ViR, sizeof(uint8_t), 1, f);

    fwrite(&x->ViT, sizeof(uint8_t), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

}


int impulse_sample_cmp(impulse_sample l, impulse_sample r)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    int32_t i, N;

    if (r == l) return 0;
    if (l == 0) return -1;
    if (r == 0) return 1;

    N = sizeof(l->IMPS_mark)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->IMPS_mark[i] < r->IMPS_mark[i]) return -1;
        if (r->IMPS_mark[i] < l->IMPS_mark[i]) return 1;
    }

    N = sizeof(l->Dos_FileName)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->Dos_FileName[i] < r->Dos_FileName[i]) return -1;
        if (r->Dos_FileName[i] < l->Dos_FileName[i]) return 1;
    }

    if (l->GvL < r->GvL) return -1;
    if (r->GvL < l->GvL) return 1;

    if (l->Flg < r->Flg) return -1;
    if (r->Flg < l->Flg) return 1;

    if (l->Vol < r->Vol) return -1;
    if (r->Vol < l->Vol) return 1;

    N = sizeof(l->SampleName)/sizeof(char);
    for (i = 0; i < N; ++i) {
        if (l->SampleName[i] < r->SampleName[i]) return -1;
        if (r->SampleName[i] < l->SampleName[i]) return 1;
    }

    if (l->Cvt < r->Cvt) return -1;
    if (r->Cvt < l->Cvt) return 1;

    if (l->DfP < r->DfP) return -1;
    if (r->DfP < l->DfP) return 1;

    if (l->Length < r->Length) return -1;
    if (r->Length < l->Length) return 1;

    if (l->LoopBegin < r->LoopBegin) return -1;
    if (r->LoopBegin < l->LoopBegin) return 1;

    if (l->LoopEnd < r->LoopEnd) return -1;
    if (r->LoopEnd < l->LoopEnd) return 1;

    if (l->C5Speed < r->C5Speed) return -1;
    if (r->C5Speed < l->C5Speed) return 1;

    if (l->SusLoopBegin < r->SusLoopBegin) return -1;
    if (r->SusLoopBegin < l->SusLoopBegin) return 1;

    if (l->SusLoopEnd < r->SusLoopEnd) return -1;
    if (r->SusLoopEnd < l->SusLoopEnd) return 1;

    if (l->SamplePointer < r->SamplePointer) return -1;
    if (r->SamplePointer < l->SamplePointer) return 1;

    if (l->ViS < r->ViS) return -1;
    if (r->ViS < l->ViS) return 1;

    if (l->ViD < r->ViD) return -1;
    if (r->ViD < l->ViD) return 1;

    if (l->ViR < r->ViR) return -1;
    if (r->ViR < l->ViR) return 1;

    if (l->ViT < r->ViT) return -1;
    if (r->ViT < l->ViT) return 1;


   /* End of automatically generated code. Manual editing below is safe. */

    return 0;
}


cached_sample cached_sample_alloc()
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    cached_sample x = calloc(1, sizeof(s_cached_sample));
    assert(x);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void cached_sample_free(cached_sample x)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    if (x->header) impulse_sample_free(x->header);

   /* End of automatically generated code. Manual editing below is safe. */

    free(x);
}


cached_sample cached_sample_alloc_from_file(FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    cached_sample x;

    x = calloc(1, sizeof(s_cached_sample));
    assert(x);

    x->header = impulse_sample_alloc_from_file(f);

    fread(&x->FileSize, sizeof(uint32_t), 1, f);

    fread(&x->Date, sizeof(uint16_t), 1, f);

    fread(&x->Time, sizeof(uint16_t), 1, f);

    fread(&x->Fmt, sizeof(uint8_t), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void cached_sample_write_to_file(cached_sample x, FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    assert(x);

    assert(x->header);
    impulse_sample_write_to_file(x->header,f);

    fwrite(&x->FileSize, sizeof(uint32_t), 1, f);

    fwrite(&x->Date, sizeof(uint16_t), 1, f);

    fwrite(&x->Time, sizeof(uint16_t), 1, f);

    fwrite(&x->Fmt, sizeof(uint8_t), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

}


int cached_sample_cmp(cached_sample l, cached_sample r)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    int cmp;

    if (r == l) return 0;
    if (l == 0) return -1;
    if (r == 0) return 1;

    if (l->header == 0)
    {
        if (r->header != 0) return 1;
    } else if (r->header == 0) return -1;
    else {
        cmp = impulse_sample_cmp(l->header, r->header);
        if (cmp != 0) return cmp;
    }

    if (l->FileSize < r->FileSize) return -1;
    if (r->FileSize < l->FileSize) return 1;

    if (l->Date < r->Date) return -1;
    if (r->Date < l->Date) return 1;

    if (l->Time < r->Time) return -1;
    if (r->Time < l->Time) return 1;

    if (l->Fmt < r->Fmt) return -1;
    if (r->Fmt < l->Fmt) return 1;


   /* End of automatically generated code. Manual editing below is safe. */

    return 0;
}


impulse_pattern impulse_pattern_alloc()
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    impulse_pattern x = calloc(1, sizeof(s_impulse_pattern));
    assert(x);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void impulse_pattern_free(impulse_pattern x)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 


   /* End of automatically generated code. Manual editing below is safe. */

    free(x);
}


impulse_pattern impulse_pattern_alloc_from_file(FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    impulse_pattern x;

    x = calloc(1, sizeof(s_impulse_pattern));
    assert(x);

    fread(&x->Length, sizeof(uint16_t), 1, f);

    fread(&x->Rows, sizeof(uint16_t), 1, f);

    fread(&x->reserved, sizeof(uint32_t), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

    return x;
}


void impulse_pattern_write_to_file(impulse_pattern x, FILE *f)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 
    assert(x);

    fwrite(&x->Length, sizeof(uint16_t), 1, f);

    fwrite(&x->Rows, sizeof(uint16_t), 1, f);

    fwrite(&x->reserved, sizeof(uint32_t), 1, f);


   /* End of automatically generated code. Manual editing below is safe. */

}


int impulse_pattern_cmp(impulse_pattern l, impulse_pattern r)
{ /* Automatically generated code.
   * Do not edit manually as all changes will be lost!
   * Generated Sat Aug 16 18:21:58 2014
   */ 

    if (r == l) return 0;
    if (l == 0) return -1;
    if (r == 0) return 1;

    if (l->Length < r->Length) return -1;
    if (r->Length < l->Length) return 1;

    if (l->Rows < r->Rows) return -1;
    if (r->Rows < l->Rows) return 1;

    if (l->reserved < r->reserved) return -1;
    if (r->reserved < l->reserved) return 1;


   /* End of automatically generated code. Manual editing below is safe. */

    return 0;
}

