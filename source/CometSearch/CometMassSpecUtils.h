/*
   Copyright 2012 University of Washington

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
*/

///////////////////////////////////////////////////////////////////////////////
//  Definitions for generic mass spectrometry related utility functions.
///////////////////////////////////////////////////////////////////////////////

#ifndef _COMETMASSSPECUTILS_H_
#define _COMETMASSSPECUTILS_H_

const double Hydrogen_Mono = 1.007825035;
const double Oxygen_Mono = 15.99491463;
const double Carbon_Mono = 12.00000000;
const double Nitrogen_Mono = 14.0030740;

class CometMassSpecUtils
{
public:
   static double GetFragmentIonMass(int iWhichIonSeries,
                                    int i,
                                    int ctCharge,
                                    double *pdAAforward,
                                    double *pdAAreverse);
   static void AssignMass(double *pdAAMass,
                          int bMonoMasses,
                          double *dOH2);

   static void GetProteinName(FILE *fpdb,
                              comet_fileoffset_t lFilePosition,
                              char *szProteinName);
};

#endif // _COMETMASSSPECUTILS_H_
