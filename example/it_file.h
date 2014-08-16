#ifndef __IT_FILE_H_D73B06
#define __IT_FILE_H_D73B06

#include <stdint.h>
#include <stdio.h>
#define MAX_CIO_SIZE 1025



typedef struct t_impulse_header {
 /* Automatically generated code.
  * Do not edit manually as all changes will be lost!
  * Generated Sat Aug 16 18:21:58 2014
  */ 

    char IMPM_mark[4];
    char SongName[26];
    uint16_t PHiligt;
    uint16_t OrdNum;
    uint16_t InsNum;
    uint16_t SmpNum;
    uint16_t PatNum;
    uint16_t CwtV;
    uint16_t Cmwt;
    uint16_t Flags;
    uint16_t Special;
    uint8_t GV;
    uint8_t MV;
    uint8_t IS;
    uint8_t IT;
    uint8_t Sep;
    uint8_t PWD;
    uint16_t MsgLgth;
    uint32_t MsgOffs;
    uint32_t Reserved;
    int8_t ChnlPan[64];
    int8_t ChnlVol[64];

 /* End of automatically generated code. Manual editing below is safe. */
 } s_impulse_header;

typedef s_impulse_header *impulse_header;

impulse_header impulse_header_alloc(); /* Do not edit this line. */

void impulse_header_free(impulse_header x); /* Do not edit this line. */

impulse_header impulse_header_alloc_from_file(FILE *f); /* Do not edit this line. */

void impulse_header_write_to_file(impulse_header x, FILE *f); /* Do not edit this line. */

int impulse_header_cmp(impulse_header l, impulse_header r); /* Do not edit this line. */

typedef struct t_impulse_instrument {
 /* Automatically generated code.
  * Do not edit manually as all changes will be lost!
  * Generated Sat Aug 16 18:21:58 2014
  */ 

    char IMPI_mark[4];
    char Dos_FileName[13];
    uint8_t NNA;
    uint8_t DCT;
    uint8_t DCA;
    uint16_t FadeOut;
    uint8_t PPS;
    uint8_t PPC;
    uint8_t GbV;
    uint8_t DfP;
    uint8_t RV;
    uint8_t RP;
    uint16_t TrkVers;
    uint8_t NoS;
    uint8_t reserved;
    char InstrumentName[26];
    uint8_t IFC;
    uint8_t IFR;
    uint8_t MCh;
    uint8_t MPr;
    uint16_t MidiBank;
    uint8_t Note_Sample_Table[240];
    envelope VolEnv;
    envelope PanEnv;
    envelope PitchEnv;
    char wastedBytes[7];

 /* End of automatically generated code. Manual editing below is safe. */
 } s_impulse_instrument;

typedef s_impulse_instrument *impulse_instrument;

impulse_instrument impulse_instrument_alloc(); /* Do not edit this line. */

void impulse_instrument_free(impulse_instrument x); /* Do not edit this line. */

impulse_instrument impulse_instrument_alloc_from_file(FILE *f); /* Do not edit this line. */

void impulse_instrument_write_to_file(impulse_instrument x, FILE *f); /* Do not edit this line. */

int impulse_instrument_cmp(impulse_instrument l, impulse_instrument r); /* Do not edit this line. */

typedef struct t_envelope {
 /* Automatically generated code.
  * Do not edit manually as all changes will be lost!
  * Generated Sat Aug 16 18:21:58 2014
  */ 

    uint8_t Flg;
    uint8_t Num;
    uint8_t LpB;
    uint8_t LpE;
    uint8_t SLB;
    uint8_t SLE;
    uint8_t NodePoints[25];
    uint8_t reserved;

 /* End of automatically generated code. Manual editing below is safe. */
 } s_envelope;

typedef s_envelope *envelope;

envelope envelope_alloc(); /* Do not edit this line. */

void envelope_free(envelope x); /* Do not edit this line. */

envelope envelope_alloc_from_file(FILE *f); /* Do not edit this line. */

void envelope_write_to_file(envelope x, FILE *f); /* Do not edit this line. */

int envelope_cmp(envelope l, envelope r); /* Do not edit this line. */

typedef struct t_impulse_sample {
 /* Automatically generated code.
  * Do not edit manually as all changes will be lost!
  * Generated Sat Aug 16 18:21:58 2014
  */ 

    char IMPS_mark[4];
    char Dos_FileName[13];
    uint8_t GvL;
    uint8_t Flg;
    uint8_t Vol;
    char SampleName[26];
    uint8_t Cvt;
    uint8_t DfP;
    uint32_t Length;
    uint32_t LoopBegin;
    uint32_t LoopEnd;
    uint32_t C5Speed;
    uint32_t SusLoopBegin;
    uint32_t SusLoopEnd;
    uint32_t SamplePointer;
    uint8_t ViS;
    uint8_t ViD;
    uint8_t ViR;
    uint8_t ViT;

 /* End of automatically generated code. Manual editing below is safe. */
 } s_impulse_sample;

typedef s_impulse_sample *impulse_sample;

impulse_sample impulse_sample_alloc(); /* Do not edit this line. */

void impulse_sample_free(impulse_sample x); /* Do not edit this line. */

impulse_sample impulse_sample_alloc_from_file(FILE *f); /* Do not edit this line. */

void impulse_sample_write_to_file(impulse_sample x, FILE *f); /* Do not edit this line. */

int impulse_sample_cmp(impulse_sample l, impulse_sample r); /* Do not edit this line. */

typedef struct t_cached_sample {
 /* Automatically generated code.
  * Do not edit manually as all changes will be lost!
  * Generated Sat Aug 16 18:21:58 2014
  */ 

    impulse_sample header;
    uint32_t FileSize;
    uint16_t Date;
    uint16_t Time;
    uint8_t Fmt;

 /* End of automatically generated code. Manual editing below is safe. */
 } s_cached_sample;

typedef s_cached_sample *cached_sample;

cached_sample cached_sample_alloc(); /* Do not edit this line. */

void cached_sample_free(cached_sample x); /* Do not edit this line. */

cached_sample cached_sample_alloc_from_file(FILE *f); /* Do not edit this line. */

void cached_sample_write_to_file(cached_sample x, FILE *f); /* Do not edit this line. */

int cached_sample_cmp(cached_sample l, cached_sample r); /* Do not edit this line. */

typedef struct t_impulse_pattern {
 /* Automatically generated code.
  * Do not edit manually as all changes will be lost!
  * Generated Sat Aug 16 18:21:58 2014
  */ 

    uint16_t Length;
    uint16_t Rows;
    uint32_t reserved;

 /* End of automatically generated code. Manual editing below is safe. */
 } s_impulse_pattern;

typedef s_impulse_pattern *impulse_pattern;

impulse_pattern impulse_pattern_alloc(); /* Do not edit this line. */

void impulse_pattern_free(impulse_pattern x); /* Do not edit this line. */

impulse_pattern impulse_pattern_alloc_from_file(FILE *f); /* Do not edit this line. */

void impulse_pattern_write_to_file(impulse_pattern x, FILE *f); /* Do not edit this line. */

int impulse_pattern_cmp(impulse_pattern l, impulse_pattern r); /* Do not edit this line. */

#endif //__IT_FILE_H_D73B06
