#!/bin/bash
awk 'BEGIN{i=1} /HEAD OF MICRO/,\
                /XI_LOCAL/ \
                 {if ($4=="dielectric") {a[i]=$1 ; b[i]=$2 ; c[i]=$3 ; i=i+1}} \
     END{for (j=1;j<i;j++) print a[j],b[j],c[j]}' OUTCAR > chi0.dat

awk 'BEGIN{i=1} /INVERSE MACRO/,\
                /XI_TO_W/ \
                 {if ($4=="dielectric") {a[i]=$1 ; b[i]=$2 ; c[i]=$3 ; i=i+1}} \
     END{for (j=1;j<i;j++) print a[j],b[j],c[j]}' OUTCAR > chi.dat