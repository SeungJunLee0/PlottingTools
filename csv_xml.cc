#include <iostream>
#include <TGText.h>
#include <string.h>
#include <fstream>
#include <string>
#include <istream>
using namespace std;




int csv_xml(){


ifstream filein;
filein.open("3dof_initial.csv");
TString a[144];
for(int i = 0;i<144;i++){
	filein>>a[i];

}
float real[144][7];

for(int as =0;as<144;as++){
TString bb;
TString aa = a[as];
for(int i =0;i<6;i++){
if(i==0){
int ii= aa.Index(",");
bb= aa(0,ii);
real[as][i]= bb.Atof();
aa.Remove(0,ii+1);
}
int ii= aa.Index(",");
if(i != 5){
bb= aa(0,ii);
real[as][i+1]= bb.Atof();
}
if(i == 5){
real[as][i+1] = aa.Atof();
}
if(i != 5)aa.Remove(0,ii+1);
}

}
filein.close();
//for(int kl =0;kl<144;kl++){
//for(int kll=0;kll<7;kll++){
//if( real[kl][kll] == 0) real[kl][kll]=0.000;
//
//}
//
//
//}


ofstream file;
file.open("Geometries/data2.xml");

//ofstream file;
//file.open("Geometries/data1.xml");

ifstream filein2;
filein2.open("Geometries/data_GEM-1100-110001_2018UL_IOV2_CMSSW106_JSON-320377-322603_dataRun2_MuAl_v1_01.xml");

char* sd;
string line;
int num=0;
if(filein2.is_open()){
for(int qw=0;qw<5176;qw++){
	while(getline(filein2, line)){
   	file<<line<<endl;
	num++;
	if(num == 5176)break;
}
if(num ==5176)break;
}

}
filein2.close();

for(int i=0;i<36;i++){
	file <<"<operation>"<<endl;
	file<<"  <GEMChamber endcap=\"1\" station=\"1\" ring=\"1\" chamber=\"";
	file<<abs(real[i][0])-100<<"\" />"<<endl;
    file<<"  <setposition relativeto=\"ideal\" x=\"";
	if(real[i][1] !=0)file<<real[i][1]<<"\""<<" y=\"";
	if(real[i][1] ==0)file<<"0.0000"<<"\""<<" y=\"";
	if(real[i][2] !=0)file<<real[i][2]<<"\""<<" z=\"";
	if(real[i][2] ==0)file<<"0.0000"<<"\""<<" z=\"";
	if(real[i][3] !=0)file<<real[i][3]<<"\" phix=\"";
	if(real[i][3] ==0)file<<"0.0000"<<"\" phix=\"";
	if(real[i][4] !=0)file<<real[i][4]<<"\" phiy=\"";
	if(real[i][4] ==0)file<<"0.0000"<<"\" phiy=\"";
	if(real[i][5] !=0)file<<real[i][5]<<"\" phiz=\"";
	if(real[i][5] ==0)file<<"0.0000"<<"\" phiz=\"";
	if(real[i][6] !=0)file<<real[i][6]<<"\" />"<<endl;
	if(real[i][6] ==0)file<<"0.0000"<<"\" />"<<endl;
    file<<"  <setape xx=\"0.0000000000\" xy=\"0.0000000000\" xz=\"0.0000000000\" xa=\"0.0000000000\" xb=\"0.0000000000\" xc=\"0.0000000000\" yy=\"0.0000000000\" yz=\"0.0000000000\" ya=\"0.0000000000\" yb=\"0.0000000000\" yc=\"0.0000000000\" zz=\"0.0000000000\" za=\"0.0000000000\" zb=\"0.0000000000\" zc=\"0.0000000000\" aa=\"0.0000000000\" ab=\"0.0000000000\" ac=\"0.0000000000\" bb=\"0.0000000000\" bc=\"0.0000000000\" cc=\"0.0000000000\" />"<<endl;
	file<<"</operation>"<<endl;
	file<<""<<endl;
}



for(int i=72;i<108;i++){
file <<"<operation>"<<endl;
	file<<"  <GEMChamber endcap=\"2\" station=\"1\" ring=\"1\" chamber=\"";
	file<<abs(real[i][0])-100<<"\" />"<<endl;
    file<<"  <setposition relativeto=\"ideal\" x=\"";
	if(real[i][1] != 0)file<<real[i][1]<<"\""<<" y=\"";
	if(real[i][1] == 0)file<<"0.0000"<<"\""<<" y=\"";
	if(real[i][2] != 0)file<<real[i][2]<<"\""<<" z=\"";
	if(real[i][2] == 0)file<<"0.0000"<<"\""<<" z=\"";
	if(real[i][3] != 0)file<<real[i][3]<<"\" phix=\"";
	if(real[i][3] == 0)file<<"0.0000"<<"\" phix=\"";
	if(real[i][4] != 0)file<<real[i][4]<<"\" phiy=\"";
	if(real[i][4] == 0)file<<"0.0000"<<"\" phiy=\"";
	if(real[i][5] != 0)file<<real[i][5]<<"\" phiz=\"";
	if(real[i][5] == 0)file<<"0.0000"<<"\" phiz=\"";
	if(real[i][6] != 0)file<<real[i][6]<<"\" />"<<endl;
	if(real[i][6] == 0)file<<"0.0000"<<"\" />"<<endl;
    file<<"  <setape xx=\"0.0000000000\" xy=\"0.0000000000\" xz=\"0.0000000000\" xa=\"0.0000000000\" xb=\"0.0000000000\" xc=\"0.0000000000\" yy=\"0.0000000000\" yz=\"0.0000000000\" ya=\"0.0000000000\" yb=\"0.0000000000\" yc=\"0.0000000000\" zz=\"0.0000000000\" za=\"0.0000000000\" zb=\"0.0000000000\" zc=\"0.0000000000\" aa=\"0.0000000000\" ab=\"0.0000000000\" ac=\"0.0000000000\" bb=\"0.0000000000\" bc=\"0.0000000000\" cc=\"0.0000000000\" />"<<endl;
	file<<"</operation>"<<endl;
	file<<""<<endl;
}

file<<"</MuonAlignment>"<<endl;
file.close();





//before reference
//
//

ofstream fileb;
fileb.open("Geometries/data1.xml");


ifstream filein2b;
filein2b.open("Geometries/data_GEM-1100-110001_2018UL_IOV1_CMSSW106_JSON-313041-320377_dataRun2_MuAl_v1_01.xml");
int num2=0;
string lineb;
if(filein2b.is_open()){
for(int qw=0;qw<5176;qw++){
	while(getline(filein2b, lineb)){
	fileb<<lineb<<endl;
	num2++;
	if(num2==5176)break;
}
if(num2==5176)break;
}

}
filein2b.close();

for(int j=1;j<73;j++){
fileb <<"<operation>"<<endl;
	int k;
	int kk;
	if(j<37){
		k=j;
		kk=1;
	}
	if(j>36){
		k=j-36;
		kk=2;
	}
	fileb<<"  <GEMChamber endcap=\""<<kk<<"\" station=\"1\" ring=\"1\" chamber=\"";
	fileb<<k<<"\" />"<<endl;
    fileb<<"  <setposition relativeto=\"ideal\" x=\"0.0000000000"<<"\""<<" y=\"0.0000000000"<<"\""<<" z=\"0.0000000000"<<"\" phix=\"0.0000000000"<<"\" phiy=\"0.0000000000"<<"\" phiz=\"0.0000000000"<<"\" />"<<endl;
    fileb<<"  <setape xx=\"0.0000000000\" xy=\"0.0000000000\" xz=\"0.0000000000\" xa=\"0.0000000000\" xb=\"0.0000000000\" xc=\"0.0000000000\" yy=\"0.0000000000\" yz=\"0.0000000000\" ya=\"0.0000000000\" yb=\"0.0000000000\" yc=\"0.0000000000\" zz=\"0.0000000000\" za=\"0.0000000000\" zb=\"0.0000000000\" zc=\"0.0000000000\" aa=\"0.0000000000\" ab=\"0.0000000000\" ac=\"0.0000000000\" bb=\"0.0000000000\" bc=\"0.0000000000\" cc=\"0.0000000000\" />"<<endl;
	fileb<<"</operation>"<<endl;
	fileb<<""<<endl;
}
fileb<<"</MuonAlignment>"<<endl;
fileb.close();
return 0;
}

