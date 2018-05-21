#!/usr/bin/python3
import webbrowser
import platform
import os

#Messages
width = os.get_terminal_size().columns
print("\n")
print("Welcome to Cleavage Site Detection.".center(width))
print("This program designed to detect cleavage sites of potyviruses.".center(width))
print("The input file is Fasta formated Amino Acide Sequence of Copmplete Polyprotein.".center(width))
print("\n")

#Read and store fasta file in the "InputFasta" variable.
ReadFileName = input("Please Enter Fasta File Name (Like, test.fasta): ".center(width))
try:
    if os.stat(ReadFileName).st_size > 0:
        ReadFile = open(ReadFileName,"r")
        InputFasta = ReadFile.read ()
    else:
        print("\n\n\n")
        print("Empty File.".center(width))
        print("Please press Enter to Exit.".center(width))
        A = input("")
        exit() 
except OSError:
    print("\n\n\n")
    print("There is No file with this name.".center(width))
    print("Please press Enter to Exit.".center(width))
    A = input("")
    exit() 


#Splites the Header form the file (SeqName) and convert the fasta formt to linear format (Seq).
SeqName = InputFasta.split('\n')[0]
Seq = ''.join(InputFasta.split('\n')[1:])




#HTML Template
htmls = """ 
<!DOCTYPE html>
 <!DOCTYPE html>
<html>
<head>
<title>Cleavage Stie Detection</title>
<style>
.SVG {
    display: block;
    margin-left:5%;
}
.center {
    display: block;
    margin:auto;
    text-align: center;
}
table {
    font-family: arial, sans-serif;
    border-collapse: collapse;
    width: 70%;
    margin:auto;
}

td, th {
    border: 3px solid #dddddd;
    padding: 8px;
    text-align: center;
}

tr:nth-child(even) {
    background-color: #dddddd;
}
</style>
</head>
<body>
<br>
<h1 class="center">Cleavage Stie Detection Results</h1>
<br>
<br>
<h2 class="center">SequName</h2>

<svg width=90% height="350" class="center">
<line x1=0 y1="195" x2=3% y2="195" stroke="black" stroke-width="15"  />
<line x1=97% y1="195" x2=100% y2="195" stroke="black" stroke-width="15"  />
<rect x=3% y="120" rx="25" ry="10" width=9.65% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=13.65% y="305">P1PoX</text>
    <text x=9.65% y="305">P1CS</text>
    <text x=6.5% y="200"style="font-size:200%;">P1</text>
    <line x1=12.65% y1="260" x2=12.65% y2="300" stroke="black" stroke-width="5"  />
	<circle cx=12.65% cy="300" r="7" stroke="black" stroke-width="3" fill="red" />

<rect x=12.65% y="120" rx="25" ry="10" width=12.81% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=26.46% y="305">HCProPoX</text>
    <text x=22.46% y="305">HCProCS</text>
    <text x=15% y="200"style="font-size:200%;">HC-Pro</text>
    <line x1=25.46% y1="260" x2=25.46% y2="300" stroke="black" stroke-width="5"  />
	<circle cx=25.46% cy="300" r="7" stroke="black" stroke-width="3" fill="red" />
    
<rect x=25.46% y="120" rx="25" ry="10" width=11.24% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=37.7% y="305">P3PoX</text>
    <text x=33.7% y="305">P3CS</text>
    <text x=30% y="200"style="font-size:200%;">P3</text>
    <line x1=36.7% y1="260" x2=36.7% y2="300" stroke="black" stroke-width="5"  />
	<circle cx=36.7% cy="300" r="7" stroke="black" stroke-width="3" fill="red" />
    
<rect x=36.7% y="120" rx="25" ry="10" width=1.68% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=39.38% y="95">6K1PoX</text>
    <text x=35.38% y="95">6K1CS</text>
    <line x1=38.38% y1="90" x2=38.38% y2="130" stroke="black" stroke-width="5"  />
	<circle cx=38.38% cy="90" r="7" stroke="black" stroke-width="3" fill="red" />
    
<rect x=38.38% y="120" rx="25" ry="10" width=20% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=59.38% y="305">CIPoX</text>
    <text x=55.38% y="305">CICS</text>
    <text x=47% y="200"style="font-size:200%;">CI</text>
    <line x1=58.38% y1="260" x2=58.38% y2="300" stroke="black" stroke-width="5"  />
	<circle cx=58.38% cy="300" r="7" stroke="black" stroke-width="3" fill="red" />
    
<rect x=58.38% y="120" rx="25" ry="10" width=1.68% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=61.06% y="95">6K2PoX</text>
    <text x=57.06% y="95">6K2CS</text>
    <line x1=60.06% y1="90" x2=60.06% y2="130" stroke="black" stroke-width="5"  />
	<circle cx=60.06% cy="90" r="7" stroke="black" stroke-width="3" fill="red" />

<rect x=60.06% y="120" rx="25" ry="10" width=6.19% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=67.25% y="305">VPgPoX</text>
    <text x=63.25% y="305">VPgCS</text>
    <text x=61% y="200"style="font-size:200%;">VPg</text>
    <line x1=66.25% y1="260" x2=66.25% y2="300" stroke="black" stroke-width="5"  />
	<circle cx=66.25% cy="300" r="7" stroke="black" stroke-width="3" fill="red" />
    
<rect x=66.25% y="120" rx="25" ry="10" width=8% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=75.25% y="305">NIaPoX</text>
    <text x=71.25% y="305">NIaCS</text>
    <text x=68.5% y="200"style="font-size:200%;">NIa</text>
    <line x1=74.25% y1="260" x2=74.25% y2="300" stroke="black" stroke-width="5"  />
	<circle cx=74.25% cy="300" r="7" stroke="black" stroke-width="3" fill="red" />
    
<rect x=74.25% y="120" rx="25" ry="10" width=14.72% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
  	<text x=89.97% y="305">NIbPoX</text>
    <text x=85.97% y="305">NIbCS</text>
    <text x=80% y="200"style="font-size:200%;">NIb</text>
    <line x1=88.97% y1="260" x2=88.97% y2="300" stroke="black" stroke-width="5"  />
	<circle cx=88.97% cy="300" r="7" stroke="black" stroke-width="3" fill="red" />
    
<rect x=88.97% y="120" rx="25" ry="10" width=8.0% height="150" style="fill:red;stroke:black;stroke-width:5;opacity:0.5" />
	<text x=92% y="200"style="font-size:200%;">CP</text>
</svg>

<br>

<table>
    <tr>
        <th>Protein Name</th>
        <th>Sequence Range</th>
        <th>Cleavage Site Type</th>
        <th>Cleavage Site</th>
        <th>Cleavage Site Position</th>
    </tr>
    <tr>
        <td>P1</td>
        <td>P1SeqReng</td>
        <td>P1/HCPro</td>
        <td>P1ClSi</td>
        <td>P1ClPo</td>
    </tr>
    <tr>
        <td>HC-Pro</td>
        <td>HCProSeqReng</td>
        <td>HCPro/P3</td>
        <td>HCProClSi</td>
        <td>HCProClPo</td>
    </tr>
    <tr>
        <td>P3</td>
        <td>P3SeqReng</td>
        <td>P3/6K1</td>
        <td>P3ClSi</td>
        <td>P3ClPo</td>
    </tr>
    <tr>
        <td>6K1</td>
        <td>6K1SeqReng</td>
        <td>6K1/CI</td>
        <td>6K1ClSi</td>
        <td>6K1ClPo</td>
    </tr>
    <tr>
        <td>CI</td>
        <td>CISeqReng</td>
        <td>CI/6K2</td>
        <td>CIClSi</td>
        <td>CIClPo</td>
    </tr>
    <tr>
        <td>6K2</td>
        <td>6K2SeqReng</td>
        <td>6K2/VPg</td>
        <td>6K2ClSi</td>
        <td>6K2ClPo</td>
    </tr>
    <tr>
        <td>VPg</td>
        <td>VPgSeqReng</td>
        <td>VPg/NIa</td>
        <td>VPgClSi</td>
        <td>VPgClPo</td>
    </tr>
    <tr>
        <td>NIa</td>
        <td>NIaSeqReng</td>
        <td>NIa/NIb</td>
        <td>NIaClSi</td>
        <td>NIaClPo</td>
    </tr>
    <tr>
        <td>NIb</td>
        <td>NIbSeqReng</td>
        <td>NIb/CP</td>
        <td>NIbClSi</td>
        <td>NIbClPo</td>
    </tr>
    <tr>
        <td>CP</td>
        <td>CPSeqReng</td>
        <td>-</td>
        <td>-</td>
        <td>-</td>
    </tr>
  </table>
  

</body>
</html>   
"""

#Library of Motifes for Cleavage Sites
LibP = ['MKHFS', 'MQHFS', 'IEHFS', 'IDHFS', 'ITHFS', 'MTHFS', 'IAHFS', 'ISHFS', 'IVHFS', 
'IIHFS', 'IMHFS', 'MVHFS', 'MIHFS', 'MHHFT', 'MHHFS', 'TKHFS', 'ATHFS', 'ITYFS', 'IRQFS', 
'MRQFS', 'IRQFT', 'IKEFS', 'IREFS', 'IEQFS', 'MEQFS', 'MQQFS', 'MIQFS', 'MVQFS', 'IVQFS', 
'IIQFS', 'MAQFS', 'ITQFS', 'MKQFA', 'IRHFT', 'IVHFI', 'ILEFS', 'VHQFA', 'LEYFS', 'IVRFA', 
'MKHYS', 'LKHYS', 'MKHYA', 'IRHYS', 'VKHYS', 'IKHYS', 'LRHYA', 'MRHYS', 'LRHYS', 'MRHYT', 
'MNHYS', 'INHYS', 'VNHYS', 'INHYA', 'VDHYS', 'IDHYS', 'MDHYS', 'IDHYA', 'IQHYS', 'VQHYS', 
'MQHYT', 'MQHYS', 'IQHYT', 'IEHYT', 'IEHYS', 'VEHYS', 'LEHYS', 'MEHYS', 'IEHYA', 'VDHYN', 
'ITHYS', 'VTHYS', 'MTHYS', 'ITHYT', 'ITHYN', 'IIHYS', 'IVHYS', 'VVHYS', 'LVHYS', 'MIHYS', 
'MVHYS', 'ILHYS', 'IMHYS', 'LVHYA', 'LIHYA', 'MVHYN', 'LIHYT', 'LCHYS', 'ICHYS', 'LSHYS', 
'VHHYS', 'IHHYS', 'MHHYS', 'IHHYA', 'IHHYT', 'VHHYT', 'THHYS', 'TEHYS', 'TKHYS', 'TIHYS', 
'TVHYS', 'TMHYS', 'CVHYS', 'TGHYS', 'MTYYS', 'LRQYS', 'MRQYS', 'MEQYS', 'LEQYS', 'IEQYS', 
'MEQYN', 'LEQYN', 'MDQYN', 'VHQYT', 'IHQYS', 'IIQYS', 'MVQYS', 'MIQYS', 'MVEYS', 'MIQYN', 
'ITQYS', 'IVQYA', 'MTEYS', 'IKYYS', 'IQYYS', 'IDYYA', 'IEDYS', 'MQHYM', 'KERYS', 'IVLYS', 
'VVPYS', 'VIPYS']

LibHC = ['YLVGG', 'YRVGG', 'YAVGG', 'YLIGG', 'FRVGG', 'HRVGG', 'YIVGG', 'YQVGG', 'YVVGG', 
'YSVGG', 'YCVGG', 'YRIGG', 'YKVGG', 'YHVGG', 'YYVGG', 'YFVGG', 'LHCGG', 'YMVGG', 'YRVGS', 
'YRMGG', 'YNVGG', 'SNVGG', 'CRVGG', 'YVIGG']

LibP3 = ['VTHQTKRK', 'VTHQVKRK', 'VEHQVKRQ', 'VEHQAKRQ', 'VEHQAKRE', 'VKHQAKRQ', 'VKHQAKRE',
'VKHQTKRR', 'VEHQTKRR', 'VEHQVKRR', 'VKHQAKRR', 'VVHQAKRQ', 'VIHQAKRQ', 'VMHQAKRQ', 'VAHQAKRQ',
'VTHQAKRQ', 'VIHQVKRQ', 'VVHQVKRQ', 'VGHQAKRQ', 'VGHQAKRK', 'VMHDAKRQ', 'VVHQARRK', 'VEHQARRE',
'VTHQAKRR', 'VSHQAKRR', 'VVHQAKRR', 'VDHQAKRK', 'VDHQAKRT', 'VVHQSKRD', 'VVHQSKRE', 'VVHQSRRE', 
'VLHQSKRE', 'VVHQNKRE', 'VVHQSKRN', 'VQHQSKRE', 'VVHQSKRY', 'VVHQSKGD', 'VKHEAKRV', 'VCHQAKRN', 
'VEHQSKRH', 'VEHQSKRS', 'VEHQAKTA', 'VEHQARSQ', 'VVYQAKSK', 'VIYQAKSK', 'VFYQAKSR', 'VEYQAKSK', 
'VEYQAKSQ', 'VVYQAKTE', 'VAYQAKTE', 'VEHQGKSR', 'VKHQGKSR', 'VEHQGKSQ', 'VTYQSKSK', 'VSFQAKTD', 
'VTYQAKTD', 'VTFQAKTN', 'VFHQAKSA', 'VVHQAKSP', 'VVHQAKSS', 'VIHQAKSD', 'VVHQAKSD', 'VIHQAKSN', 
'VFHQAKSN', 'VIHEAKSN', 'VIHQAKTV', 'VVHQAKTV', 'VVHQAKTT', 'VAHQAKTV', 'VVHQAKTQ', 'VVHQAKTK', 
'VIHEGKSN', 'VIHEGKSS', 'VIHEGKSR', 'VIHEGKSK', 'VIHEGKSH', 'VIHENKSR', 'VIHEHKSK', 'VAHQSKNP', 
'VVHQSKNP', 'VKHQAKNP', 'VQHQAKGL', 'VQHQAKGM', 'VQHQAKGV', 'VKHQAKGV', 'VKHQAKTH', 'GRHQAKTH', 
'VVEQGKGP', 'VTYQGKSP', 'VQHQGKKR', 'VEHQKKGS', 'VEHERKGY', 'VEHQSKGE', 'VEHQAVKR', 'VEHQATKR', 
'VEHQAAKR', 'VEHQANKR', 'VEHQASKR', 'VQHQASKR', 'VDHQASKR', 'VKHQASKR', 'VGHQASKR', 'VNHQARRP', 
'VEFQHKRK', 'AEFQHPRP', 'VKFQYKKK', 'VQHQHKSK', 'VKFQVKNQ', 'FKFQHKGK', 'VLFQAKAS', 'VEFQAKNT', 
'VEFQARST', 'VQFQAKPD', 'AQFQAKPD', 'VEFQAKPS', 'YIFQAKTD', 'VKLQARSQ', 'VSWQAKNA', 'VATQSKTV', 
'VETQAKTA', 'VETQAKTH', 'VQTQGKTA', 'VSVQAKNA', 'VSVQAKSA', 'VSVQAKTA', 'VSAQAKNA', 'VSVQAKNT', 
'VSAQAKTA', 'VSAQAKTV', 'VSAQVKTA', 'VSVQVKTA', 'VSVQTKTA', 'VFAQAKTA', 'VYAQAKTA', 'VSTQGKTA', 
'VATQAKTA', 'VATQAKTG', 'VTTQAKTA', 'VSTQAKTA', 'VTPQAKTA', 'VTPQAKSA', 'VAPQAKSA', 'VTAQAKSA', 
'VSAQAKSA', 'VATQAKSA', 'VSTQAKSA', 'VHLQAKTA', 'VNLQAKTA', 'VTLQAKTA', 'VICQAKTS', 'VTCQAKTS', 
'VSCQAKTP', 'VSAQAKTS', 'VEVQAKTA', 'VEAQAKTA', 'VSVQAKGA', 'VTTQGKTG', 'VELQAKTQ', 'VDTQAKTQ', 
'GDTQAKTQ', 'VTTQAKTE', 'VSMQAKTK', 'VHVQGKTA', 'YEFQAKSN', 'YTFQAKPN', 'YVFQAKPN', 'YKFQAKPN', 
'VSFQAKSK', 'FVMESKSN', 'ITLQSKGR', 'VEHQHQRS', 'VQHQSKVS', 'VRLQAKKE', 'VNFQSKTV', 'VRLQSKTY', 
'VEYQANKV', 'MEFQAKGD', 'MEYQAKGD', 'ESTQSKEA', 'VGHQDFKS', 'VRHQRSTP', 'VRHQRATP', 'ARHQRSTP', 
'VKHQKSTP', 'VEHQKSTA', 'VSHQKATA', 'VEHQQSTT', 'VEHQKSTS', 'VEHQKSTL', 'VHHQRGTA', 'VVHQRSTE', 
'VIHQRSTE', 'VTHQRSTE', 'VAHQRSTP', 'VSHQGSTE', 'VMHQDSKA', 'VVHQDSKS', 'VKHQDSKS', 'VVHQASKS', 
'VVFQDAKS', 'VEHQKNDQ', 'VVHQRHTS', 'VVHQKSFD', 'VHHQKVTE', 'VKLQQSKT', 'CNYQAKNV', 'TEYESKSA', 
'VVHQVKQH', 'LVEQAKQP', 'LIEQAKQP', 'LVEQAKRP', 'FSIQAKKH', 'VSFQAGTP', 'ITLQKGKK', 'TTLQKGRQ']

Lib6K1 = ['VVHQSADV', 'VIHQSADV', 'VTHQSIEL', 'VAHQSIEL', 'VVHQSIDV', 'VTHQSLEL', 'VTHQSLDL', 
'VVHQSLDL', 'VTQQSMDV', 'VKHEGSQI', 'VHHQMSTI', 'VEHQGTQV', 'VYHQSLDE', 'VYHQSLDD', 'VFHQSLDD', 
'VYHQALDD', 'VYHQSIDD', 'VYHQSIDE', 'AYHQSLDD', 'VHHQSLDD', 'VHHQSIDD', 'VHHQNLDD', 'VQHQSLDD', 
'VRHQSLDD', 'VRHQSVDE', 'VRHQSVDD', 'VRHQSIDD', 'VKHQSLDD', 'IRHQSVDE', 'VRHQSLDE', 'VIHQSLDD', 
'VVHQSLDD', 'VMHQSLDD', 'VAHQSLDD', 'VSHQSLDD', 'VGHQSLDD', 'VTHQSLDD', 'VEHQSLDD', 'VRHQSLND', 
'VKHQALDD', 'TKHQSLDD', 'VRHQSLDT', 'VQFQSLDD', 'VHFQSLDD', 'VQYQSLDD', 'VRVQSLDD', 'VRVQSLDE', 
'VRIQSLDE', 'VKVQSLDE', 'VKMQSLDE', 'VQVQSLDE', 'VKIQSLDE', 'VRLQSLDE', 'VKLQSLDE', 'VKVQSLDD', 
'VKIQSLDD', 'VKLQSLDD', 'VRLQSLDD', 'VRIQSLDD', 'VKVQSVDE', 'VRAQSLDE', 'VKAQSLDE', 'VRPQSLDE', 
'VRPQSLDD', 'VKVQGLDE', 'VQIQSLDE', 'VQMQSLDE', 'VQIQSVDE', 'VQTQSLDE', 'VTVQSLDE', 'VRYQSLDE', 
'VKYQSLDE', 'VKYQSLDD', 'VRMQSLDD', 'VRVQGLDD', 'VMIQSLDE', 'VHFQSLDE', 'VQHQAIDD', 'VRCQSLDE', 
'VRCQSIDD', 'VRCQNIDD', 'VKFQSIDD', 'VSFQSIDD', 'MKFQSLDD', 'MRFQSLDD', 'VRFEALDD', 'VRLQGLED', 
'VRFQGLED', 'MTFQSLDD', 'VRFQSLDT', 'CRFQSLDT', 'VYHQALNE', 'VYHQALND', 'VYHQTLND', 'VYHQTIND', 
'VYHQTLNE', 'VHHQTLND', 'VHHQTLNE', 'VHHQALND', 'VYHQTLNV', 'VYHQGLSE', 'VFHQGLSE', 'VYHQALSE', 
'VFHQSIDD', 'VFHQSVDE', 'VEFQNLDE', 'VGFQNLDE', 'VNHQSMDD', 'VNHQSVDD', 'VYHQSTDD', 'VHYQALDS', 
'VHYQALDE', 'VQYQALDT', 'VQYQALDA', 'VNYQALDT', 'VNYQALDP', 'VQFQSLEN', 'VYHQLDEI', 'VYHQLDDI', 
'VTQQSVDV', 'VAQQSVDV', 'VVQQSVDV', 'VMQQSVDV', 'VVQQSVNV', 'VTHQSVDI', 'VTHQSVEL', 'YKFQSLDD', 
'FKFQALDA', 'YRFQSLDT', 'YKFQSLDT', 'VAHQSLDT', 'VNHQSLDT', 'VNHQSIDT', 'VRHQGSLD', 'IRLESSLD', 
'TRLESSLD', 'MLHQSLDD', 'MTLQSLDD', 'VNHQSIDS', 'IYTQSLDD', 'VYTQSLDD', 'IHLQSLDD']

LibCI = ['VQHQSTHE', 'VQHQSTHD', 'VQHQSKHE', 'VQHQSKHD', 'VQHQSGHE', 'VYHQSTHE', 'VYHQTTHS', 
'VLHQSKEE', 'VMHQNKEE', 'VMHQSIDD', 'VMHQSKQD', 'VLHESRDD', 'VLHQSKDD', 'VLHQSQDD', 'VVHQSKDE', 
'VMHQSTEG', 'VMHQSTDG', 'VLHQSREG', 'VLHQSRDG', 'VLHESKEG', 'VMHQNAEG', 'VLHQSVEG', 'VIHETREG', 
'VIHETRDG', 'VIHENKEG', 'VIHENKEN', 'VIHENKED', 'VMYQSTEE', 'VHHQSEKT', 'VYHQSEKA', 'VYHQSEKE', 
'VYHQSERE', 'VHHQNTND', 'VHHQSTND', 'VHHQNTSD', 'VHHQNTTD', 'VHHQNTSE', 'VHHQNTNE', 'VHHQSTNE', 
'VHHQSTSE', 'VHHQSTTE', 'VHHQNTNN', 'VHHQSAND', 'VHHQSVND', 'VHHHNTND', 'VHHQNISD', 'VHHQSASE', 
'VHHQSENE', 'VNHQSTNE', 'VHHQNTNG', 'VHHQSTNG', 'VNHQNTND', 'VHHQATTS', 'VHHQSTTS', 'VHHQATTA', 
'VHHQAVTS', 'VHHQSVTS', 'VHHQAATS', 'VHHQSATS', 'VHHQVATS', 'VHHQVATT', 'VHHQATPS', 'VHHQSTGA', 
'VHHQSKES', 'VHHQSKSS', 'VHHQSKDA', 'VHHQSKGA', 'VHHQKKNS', 'VHHQSKHT', 'VHHQSKHA', 'VHHQSKHQ', 
'VHHQPKHK', 'VHHQSKRD', 'VHHQSKKD', 'VQHQNKNS', 'VHHQSKNE', 'VHHQSKRL', 'VVHQSKDS', 'VQHQSYNE', 
'VHHQTKEG', 'VHHQSKEG', 'VHHQNKEG', 'VHHQTKES', 'VQHQTKEG', 'VQHQSEDA', 'VQHQSTEA', 'VQHQSAEA', 
'VQHQSKDA', 'VQHQSKEA', 'VQHQNKEA', 'VYHQSKDS', 'IYHQSKEA', 'IYHQSKGA', 'VYHQSKES', 'VQHQSEEE', 
'VTHQSSFE', 'VTHQSRQE', 'VTHQSNQD', 'VTHQNANE', 'VLHQSSNA', 'VTHQSTHG', 'VTHQSSGG', 'VHYQNKND', 
'VLHQTKDS', 'VLHQTKDA', 'VLHQTKND', 'VLHQTKSD', 'VYHQSTQA', 'VLFQSKED', 'ALFQSKEA', 'VLYQGKDN', 
'VMYQGKDA', 'VIHQGMDA', 'IIHQGMDA', 'VIHQGLDA', 'VLHQGMDA', 'VIHQGVDA', 'VIHQGMDT', 'VVHQGLDA', 
'VIHQGLDE', 'VINQGLDA', 'VIHQGLDS', 'VFHQGLDS', 'VIHQGVDE', 'VIHQGLHS', 'VIHQSTEQ', 'VQFQTLES', 
'LEFQSLET', 'VNFQSLED', 'VHFQSKND', 'VHFQSKSG', 'LHFQSEVE', 'MMFQSENE', 'MMYQSENE', 'MMYESENE', 
'MMFESEND', 'MMYESEND', 'MMYESEID', 'LQFESLQE', 'LQFESLQG', 'LQFESMQG', 'LQFESVQG', 'LQFESSQG', 
'LQFESTQG', 'LQFESASE', 'VEFQSQAG', 'ITFQSSKG', 'VRFQSESE', 'IRFQSKEE', 'VRLQSKGE', 'VRLQSKGA', 
'VRLQSKEA', 'VHLQSKEE', 'VHLQSKGE', 'VRLQGKEE', 'VRMQSKSE', 'VRLQSKSE', 'VRLQSRSE', 'VRLQSQSE', 
'VRLQGKAE', 'VRLQGRAE', 'VRLQSKAE', 'VRLQSKNE', 'VRLQGKSE', 'VRLQGKNE', 'VRLQGKGE', 'VRLQSKEE', 
'VQLQSKEE', 'VQLQSKQE', 'VQLQSKHE', 'VQLQSRHE', 'VQLQGKHE', 'VQLQSNHE', 'VQLQSTHE', 'VQLQSAHE', 
'VQLQSKYE', 'VQLQSTYE', 'VCLQSKHE', 'VCLQSKQE', 'VVLQSKQE', 'VMLQSKQE', 'VQFQSGTQ', 'VQFQSKTQ', 
'VQFQSKMQ', 'VQFQNKEE', 'VQFQSEEE', 'VQFQNKSE', 'VQFQNKNE', 'VQFQSRSE', 'VQFQSRNE', 'ITFQSRNE', 
'VEFQGEDE', 'VQYQSATD', 'VQYQDKKS', 'VQYQDNKE', 'VQYQSKNE', 'LQFEDERT', 'IYLQSDSE', 'VYLQSDSE', 
'IYLQSDGE', 'IYHQSEGE', 'VQHQGVNE', 'VQHQGINE', 'VRHQSVDG', 'VYHQSVDG', 'VFHQSVDG', 'VYHQGVDG', 
'VYHQSVNG', 'VFHQNVDG', 'VYHQNVDG', 'VYHQETNG', 'VYHQEANG', 'VYHQSQDG', 'VFHQGENG', 'VYHQGEHG', 
'VHHQTLSG', 'VFHQSGSD', 'VQHQSAPG', 'VQHQSTPG', 'VQHQTSSK', 'VQHQTASK', 'VQHQDTKS', 'VQHQDTGA', 
'VRCQSKSE', 'VRLQHKED', 'IGLQSKRE', 'VRSVSKQE', 'VLHESAPE', 'VNYQSSND', 'VNYQSAND', 'VNYQSTND', 
'VEFQNSDD', 'VEYQTKEQ', 'VHHQGRDL', 'VLTKLATS', 'CNCRASTK']

Lib6K2 = ['VFHQGFSA', 'VYHQGFSA', 'VHHQGFSA', 'VEFQGKRE', 'VQFQGKRE', 'VEFKGKGE', 'AGHNSRKE', 
'VRYQGKGF', 'VHHEAKGK', 'VHHEARGK', 'VYHEAKGK', 'VYHEARGK', 'VFHEAKGK', 'VFHQAKGK', 'VIHEAKGK', 
'VVHEAKGK', 'IVHEAKGK', 'VAHEAKGK', 'VTHEAKGK', 'VTHEARGK', 'VTHESKGK', 'VTHEAKSK', 'VTHEAKCK', 
'VIHEAKSK', 'VYHESKSK', 'VQHQAKSK', 'VQHQAKNK', 'VEHQAKNK', 'VKFQAKNK', 'VRFQAKNK', 'VRYQAKNK', 
'VRYQARNK', 'VKYQARNK', 'VQYQAKNK', 'VTYQAKNK', 'VNHQAKSK', 'VEHEGKSK', 'VQHEGKSK', 'VEHQAKSK', 
'VRHQGKDK', 'VRHQGKGK', 'IRHQGKGK', 'VTHQGKEK', 'VAHQGKEK', 'VKHQGKEK', 'VTHQGKNK', 'VIHQGKEK', 
'VLHQGKEK', 'VLHQGREK', 'VQHQGREK', 'VSHQARNK', 'VSHQAKNK', 'VSHQGKNK', 'VAHQGKNK', 'VRHQGKNK', 
'VCRQGKNK', 'VCHQGKNK', 'VLHQGKNK', 'VLHQGRNK', 'VIHQGKNK', 'VSYQGKNK', 'VEYQGKNK', 'VEHQGKNK', 
'VEHQGRNK', 'AEHQGKNK', 'VTHQGRSK', 'VTHQGKSK', 'VTHQGGSK', 'VTHQGKGK', 'VVHQGKRK', 'VSHQGRNK', 
'VSHQGKTK', 'VSHQGKSK', 'VQHQGKNK', 'VHHQGKNK', 'VHHQGRAK', 'VHHQGKAK', 'VHHQGRSK', 'VSHQGRSK', 
'VTHQGKAK', 'VVHQGRDK', 'VVHQGRHK', 'VEHQGMSK', 'VTHQGMSK', 'VVHQARNK', 'VEHQASTK', 'VIHQGMGK', 
'VSHQGMGK', 'VYHQGFNK', 'VFHQGYNK', 'VEHQGYNK', 'VSHQGYNK', 'VQHQGYSK', 'VYHQGYNK', 'VYHQGQNK', 
'VHHQGFGK', 'VAFQGYNK', 'VSFQGYNK', 'ISFQGYNK', 'VKHEAKTK', 'VRHQGYSK', 'VNHEGKRK', 'VHHEGKRK', 
'VYHQGFSK', 'VNHQAQKK', 'VDHQAQRK', 'VDHQAQKK', 'VDHQAQSK', 'VDHQAQNK', 'VKFEGKTK', 'VKLEGKSK', 
'FKFQGKSK', 'YKFQGKSK', 'FSFQGNNK', 'FVFQGKNK', 'FIFQGKNK', 'FTFQGKNK', 'FSFQGKNK', 'CTFQGKSK', 
'YSFQAKNK', 'FLFQAKNK', 'VAFEGKRK', 'VHFQGLNK', 'VYHQGNTK', 'VSPQGKNK', 'VNLQAQSK', 'VRYQGKRQ', 
'VKYQGKRQ', 'VFHQGFSV', 'MDYQGKNY', 'VRHQGLNG', 'VQYQAKNR', 'VSHQGRSR', 'VVHQGFNR', 'VIHQGFNR', 
'VAHQGFNR', 'VTHQGFNR', 'AVHQGFNR', 'VQHQGFNR', 'VSHEGWNR', 'VNHQAQKR', 'VSHQAQGR', 'FVFQGKNR', 
'VQYQGKRR', 'VEFQGKKR', 'VEFQGWKR', 'VTTQGRKR', 'VTTQGKKR', 'VSTQGKKR', 'VATQGKKR', 'VSTQGRKR', 
'VNTQGKKR', 'VVTQGKKR', 'VITQGKKR', 'VATQGRKR', 'VITQGRKR', 'VVTQGRKR', 'VTAQGRKR', 'VTAQGKKR', 
'VAAQGKKR', 'VPTQGKKR', 'VTTQGNKR', 'VSTQGNKR', 'VTTQGRNR', 'VTTQGKNR', 'VRVESKKR', 'VRIESKKR', 
'VTTQGKKD', 'VYFQGKKN', 'ISLEGKKN', 'ITLQGRKN', 'IALQGRKN', 'VTYQGKGN', 'VAHQGKSS', 'VSHQGKRS', 
'VKHQGKNS', 'VMHQGKSS', 'VAFQGIIS', 'ITLQGKMS', 'MEYQGKNH', 'MNYQGKNH', 'VKFEGAKH', 'VKFQGKSR', 
'VRFQGKSR', 'VHYQAKSR', 'VHHEAKGT']

LibVpg = ['VNHESASL', 'VNHESVSL', 'VNHESESL', 'VDHESASM', 'VKHESASL', 'VEHESTSL', 'VQHESASL', 
'VQHESALL', 'VQHESSSL', 'VDHESSSM', 'VDHESNSM', 'VGHESSSM', 'VDHESTSM', 'VGHESNSM', 'VDHESCSM', 
'VDHESKSL', 'VGHESKSL', 'VGHEGKSL', 'VDHDSKSL', 'VDHESRSL', 'VEHESKSL', 'VEHESRSL', 'VTHESKSL', 
'VEFENKST', 'VEFENRST', 'VDFENRST', 'VEFESKAM', 'VEFESKAL', 'LVFESASN', 'HEFESKST', 'VTHEARSL', 
'VEHEARSL', 'VEHEAKSL', 'VEHEAHSL', 'VGHEAHSL', 'VAHEAKSL', 'VDHEAKSL', 'VTHEGDSL', 'VIHEGDSL', 
'VIHESKSL', 'FEFEGKSL', 'VTHEGKAL', 'VGHEAYAN', 'VGHEARSL', 'VSHESKSL', 'ATHEGLSM', 'TTHEGLSM', 
'TVHEGESL', 'ATHEGKSM', 'VAFESLSM', 'VSFESLSM', 'VAFESKAL', 'VSFESKAL', 'VEFESTSM', 'VSHEAKSM', 
'IAHEGNSL', 'FKHESKAL', 'VEHEGKNL', 'VKHESKTL', 'IKHESKTL', 'IQFEAKTK', 'VTHESNAL', 'VHHEGKSL', 
'VYHEGKSL', 'VNHEGKSL', 'VHHEGRSL', 'VLHEGKSL', 'VTHEGKSL', 'VAHEGKSL', 'VTHEGRSL', 'VVHEGKSL', 
'VQHEGKSL', 'VEQEAESL', 'VEHEGKSL', 'VVHESKSL', 'VVHEAKSL', 'VVHESKSP', 'VVHEAASL', 'VKHEAKTL', 
'VKHEAKTI', 'VAHEAKAL', 'VEHEAKAL', 'VVHESKAL', 'ASHESKSL', 'VEHESSSL', 'VDHESQTL', 'MTFESSLK', 
'FDFESLSK', 'FEFESISK', 'AEFESLNR', 'VDFENKSA', 'VDLKNKSA', 'VDFENKSS', 'VAYEAKSL', 'VSFEAKSA', 
'VSFEAKST', 'VSFEAKSV', 'VQFEAKSA', 'VTFEAKSA', 'VQTESKSV', 'VDIESKSI', 'VGIESKSI', 'VAVESKSI', 
'VTTESKSI', 'VAVENKFC', 'VAVESRSI', 'VAVESKSV', 'VVVESKSV', 'VEMESKSV', 'VEMESKSI', 'VEVESKSV', 
'VEVEIKSV', 'VEIESKSV', 'VDVESKSV', 'VELESKSV', 'VKVESKSV', 'VTTESKSV', 'VELESKST', 'VDLESRSV', 
'VEVEGKSV', 'VEMEGKSV', 'VETESKSV', 'VELESKSI', 'VGVESKST', 'VGVESQST', 'VELESKYI', 'VAMEGKSV', 
'WQMEGKSV', 'VNLESKSV', 'VREEGKSI', 'VASEGKSI', 'VAPEGKSI', 'VATEGKSM', 'VRTEGKSM', 'VQLEGKSL', 
'LTFEGESL', 'LMFEGESL', 'IELEGVSL', 'IELEGASL', 'IKLEGVSL', 'VAHESKSM', 'VAHESKPM', 'VTHEAKSM', 
'VEHEAKSM', 'VEHESKSM', 'VLHEAKSM', 'VEYEAKSM', 'VAHEAKSM', 'VTHESKSM', 'VEHEGVAT', 'VEHEGTSA', 
'VLHEGASM', 'VSFEGASS', 'VKYEGKTT', 'VEYEGKTA', 'VRTEAASL', 'VEHEGKAI', 'VDHETKSI', 'VVFESKAV', 
'VEFEGKSL', 'VSYESKAM', 'VKEESKSL']

LibNIa = ['VQEQGLSE', 'VQEQAKTE', 'VQEQARTE', 'VQEQGRTE', 'VQEQGKTE', 'VMEQGKTE', 'VSEQSKYE', 
'VRQQMKKE', 'VRQQMKRE', 'VHPQMKRE', 'VTVQGRKE', 'VTVQGKKE', 'VTAQGKKE', 'VTAQGRKE', 'VAVQSRKE', 
'VTVQSRKE', 'VTVQSKKE', 'VVVQSKRE', 'VIVQSKRE', 'VVIQSKKE', 'VTTQSKQE', 'VTMQSKQE', 'VATQSKQE', 
'VCTQSKQE', 'VKTQSKRE', 'VETQSKRE', 'VQTQSKVE', 'VQTQSKIE', 'VRTQSRDE', 'GCTQSKQE', 'VEFQHRDE', 
'MKFQGLEE', 'VGMQSHDE', 'VREQGQNF', 'VTEQGMTF', 'VFEQSGSP', 'VYAQTEHQ', 'VYPQSGTQ', 'VYAQDKRQ', 
'VNEQAQVQ', 'VCEQAHIQ', 'VSEQCKVQ', 'VATQSKQQ', 'VATQNKQQ', 'VATQSKRQ', 'VETQSKQQ', 'VETQSEQQ', 
'VAVQSSRQ', 'CSFQASAQ', 'IVVQAQTQ', 'IVIQANMQ', 'VCAQSSNQ', 'LATQIKQQ', 'VYSQSGEV', 'VTMQGLSV', 
'VAFQAQDY', 'VYAQTQQK', 'TFEQSGKK', 'VREQGEEK', 'VQEQGEEK', 'VSEQASEK', 'VCEQASEK', 'VREQASDK', 
'VEEQSHEK', 'VTTQSKRK', 'VVVQSQRK', 'VSMQSREK', 'AEFQSSEK', 'WNFQAGFK', 'WEFQSGYK', 'WEFQSGHK', 
'WEFQSGNK', 'WGFQEKSK', 'VQEQSGEA', 'VKEQACTA', 'VECQAEVA', 'VYTQMARG', 'VYSQMARG', 'VYAQMARG', 
'VYSQMSRG', 'VYSQMERG', 'VYAQMERG', 'VYAQSYDG', 'VFNQSIKG', 'AMYQHGRG', 'VYAQSKTW', 'ATTQSKKW', 
'VYEQSKER', 'VYEQSDTR', 'VFQQSQQR', 'VFEQSGSR', 'AFEQSGSR', 'VFEQSGGR', 'VEEQSHER', 'VSEQGSIR', 
'VRTQGEKR', 'VYSQGEKR', 'VRWQGTSR', 'VCAQSSNR', 'VYSQMERS', 'VVEQGYSS', 'VIEQGQDS', 'VYEQGSES', 
'VYEQGQES', 'VYTQGCDS', 'VHTQGCDS', 'VYTQGYDS', 'VYTQGFDS', 'VQEQSQES', 'VREQSNNS', 'VREQSKSS', 
'VREQSKNS', 'VHEQSKNS', 'VREQGENS', 'VVEQAKHS', 'VIEQAKHS', 'VAEQAKHS', 'VTEQAKHS', 'VVEQVKHS', 
'VVEQANHS', 'VLQQAKHS', 'VVEQAKLS', 'VREQASHS', 'VREQAHTS', 'VRERGRKS', 'VGFQSKES', 'VQLQGFQS', 
'VQLQGSQS', 'IKVQAVES', 'VAMQAYDS', 'VYAQTQQT', 'VYNQSKTT', 'VYNQAKTT', 'VYNQSQTT', 'VYNQSRTT', 
'VYTQSKTT', 'VYAQSKTT', 'VHTQSKTT', 'VHNQSKTT', 'VVEQGSTT', 'VIEQGSTT', 'VREQGRST', 'VREQAQST', 
'VREQGQST', 'VREQGRNT', 'VHEQGRKT', 'VREQGENT', 'VREQGKNT', 'VREQASNT', 'VREQSAHT', 'VEEQCKVT', 
'VEEQCKIT', 'VEEQCRVT', 'VEEQCKAT', 'VEEQCEVT', 'VEEQCGVT', 'VEEQCGTT', 'VEEQRKVT', 'VQLQGNQT', 
'VAVQGAQT', 'VVEQSLQT', 'VIEQSLQT', 'MQNVSEDT', 'MHNVSEDT', 'VSNESADT', 'ISNESADT', 'VSNESTDT', 
'VYAQTQQD', 'VYAQTRSD', 'VYAQTKSD', 'VYTQTRSD', 'VYAQARSD', 'VYTQSRTD', 'VYAQAKHD', 'VQEQGFSD', 
'VREQAVQD', 'VAMQSKRD', 'VSVQSRKD', 'VAVQSKKD', 'VSVQSKKD', 'VAVQSRTD', 'VSTQSKRD', 'VKTQSRHD', 
'VRTQSRDD', 'VGLQSRED', 'VQFQSKQD', 'VELQSKSD', 'VEYQSGQD', 'VGYQSGQD', 'VRVQANTD', 'VIEQGKRD', 
'VKIQSSQC', 'VHTQSKTH', 'VYEQNQTH', 'VFEQSGSH', 'VYNQSINH', 'VTEQGIQH', 'VTEQGMTH', 'VTEQGLMH', 
'VTFQSSEH', 'VSFQSSEH', 'VHEQAGIH', 'VYAQTQQN', 'VYAQTRQN', 'VYAQTQHN', 'VYAQMQQN', 'VYSQSLNN', 
'VYPQSARN', 'VSEQSKTN', 'MREQSGTN', 'LSFQSAKN', 'LSFQSANN', 'LGFQSSRN', 'VKAQGLEN']

LibNIb = ['SEVYHQ', 'FDVYHQ', 'LDVFHQ', 'SEVFHQ', 'VEVYHQ', 'LEVYHQ', 'VCVYHQ', 'ACVYHQ', 'TCVYHQ', 
'MCVYHQ', 'ICVYHQ', 'VSVYHQ', 'VRVYHQ', 'ECVYHQ', 'AFVYHQ', 'IDVFHQ', 'IDVHHQ', 'IDVRHQ', 'IDVKHQ', 
'EEVIHQ', 'EEVVHQ', 'EDVIHQ', 'EDVFHQ', 'EEVFHQ', 'DEVFHQ', 'EDVFYQ', 'EDVVHQ', 'EDVYHQ', 'VYVYHQ', 
'ETVYHQ', 'DEVYHQ', 'NEVYHQ', 'EEVWHQ', 'YEVHHQ', 'YEAHHQ', 'YEVYHQ', 'CEVHHQ', 'YEVRHQ', 'YEVVHH', 
'FEVHHQ', 'FSVSHQ', 'YDVYHQ', 'YEVSHQ', 'YEVYHE', 'FEVRHR', 'FEVFHE', 'MEVYHQ', 'LSVYHQ', 'LTVYHQ', 
'EQVYHQ', 'TIVYHQ', 'TTVYHQ', 'ANVHHQ', 'ADVHHQ', 'NNVYHQ', 'NNVHHQ', 'YSVHHQ', 'NSVHHQ', 'EPVYHQ', 
'EPVYHL', 'ELVYHQ', 'NIVIHQ', 'NIVVHQ', 'NIVTHQ', 'NVVVHQ', 'NVVMHQ', 'NIVMHQ', 'DVVVHQ', 'DVVIHQ', 
'DIVVHQ', 'DIVIHQ', 'DTVIHQ', 'DSITFQ', 'DEVTMQ', 'MKFVFQ', 'DEVVLQ', 'DKVVGQ', 'VQVFHQ', 'HTVFHQ', 
'LRVIHQ', 'DDVYHQ', 'GEVTHQ', 'GEVAHQ', 'GEVDRI', 'SEVIHQ', 'DEVDHQ', 'DMVYFQ', 'DIVYFQ', 'LLVYHE', 
'LLVYYE', 'LLVHHE', 'LVAYHE', 'LVVYHE', 'LVVYHQ', 'LMVYHQ', 'LLVYHQ', 'LLVQHG', 'EIVAFQ', 'EDVMLQ', 
'EDVVLQ', 'EEIYLQ', 'EDIYLQ', 'EIVHYQ', 'KEVRYQ', 'SEVRYQ', 'KAVRYQ', 'KVVRYQ', 'DEVRYQ', 'DEVVYQ', 
'DEFCFQ', 'EEFVFQ', 'DIFEYQ', 'EIFEYQ', 'EVFEYQ', 'ETFEYQ', 'DTFVFQ', 'ETFVFQ', 'ENLYFQ', 'ETLYFQ', 
'ESVHLQ', 'DTVHLQ', 'EQVYLQ', 'ESVSLQ', 'ESVALQ', 'ETVLLQ', 'ETVSLQ', 'EAVSLQ', 'EDVILQ', 'ESVSTQ', 
'ESVYLQ', 'CYVSHQ', 'EEVIFQ', 'DIVTYQ', 'QFVEHQ', 'DFVLHQ', 'EDVHFQ', 'DEVHFQ', 'EHVYHQ', 'FEVSHQ', 
'LEVEHQ', 'IDVEHQ', 'VDVEHQ', 'LDVRHQ', 'FDVRHQ', 'MEVRHQ', 'LCVYHQ', 'NFMMHQ', 'NCVLHQ', 'IEVHFQ', 
'IEVYFQ', 'IKVRLQ', 'LTCRFQ', 'LVCRFQ', 'LSCKFQ', 'IECRFQ', 'IECYFQ', 'IECCFQ', 'ILCCFQ', 'FTCFFQ', 
'EIVKHQ', 'EIVSHQ', 'LSCAFQ', 'EDVSHQ', 'NVVEHQ', 'DTVMLQ', 'DTVVLQ', 'DTVILQ', 'EYVSLQ', 'QRVAFQ', 
'QRVSFQ', 'ESVCYQ', 'NWVEFQ', 'ETVRFQ', 'DVVTLQ', 'LAVTHQ', 'MGACSR', 'SYVSYQ', 'PYVSHQ', 'EEIHLQ', 
'GIVLVQ', 'DNCIFQ', 'INVRFE', 'LYVYHQ', 'LFVYHQ']


#Detecting the Positions and Sequences of Cleavage Sites
for ihc in LibHC: 
    if  Seq.find(ihc) != -1:
        HCProPosition = Seq.find(ihc)+4
        HCProSequence = ihc
        HCProCS = Seq[Seq.find(ihc)+3]+"/"+Seq[Seq.find(ihc)+4]
        HClocation = Seq.find(ihc)
        
for ip1 in LibP: 
    if  Seq.find(ip1) != -1 and Seq.find(ip1) < HClocation:
        P1Position =Seq.find(ip1)+4
        P1Sequence = ip1
        P1CS = Seq[Seq.find(ip1)+3]+"/"+Seq[Seq.find(ip1)+4]

for ip3 in LibP3: 
    if  Seq.find(ip3) != -1 :
        P3Position = Seq.find(ip3)+4
        P3Sequence = ip3
        P3CS = Seq[Seq.find(ip3)+3]+"/"+Seq[Seq.find(ip3)+4]

for i6k1 in Lib6K1: 
    if  Seq.find(i6k1) != -1 :
        SixK1Position = Seq.find(i6k1)+4
        SixK1Sequence = i6k1
        SixK1CS = Seq[Seq.find(i6k1)+3]+"/"+Seq[Seq.find(i6k1)+4]

for ici in LibCI: 
    if  Seq.find(ici) != -1 :
        CIPosition = Seq.find(ici)+4
        CISequence = ici
        CICS = Seq[Seq.find(ici)+3]+"/"+Seq[Seq.find(ici)+4]

for i6k2 in Lib6K2: 
    if  Seq.find(i6k2) != -1 :
        SixK2Position = Seq.find(i6k2)+4
        SixK2Sequence = i6k2
        SixK2CS = Seq[Seq.find(i6k2)+3]+"/"+Seq[Seq.find(i6k2)+4]

for ivpg in LibVpg: 
    if  Seq.find(ivpg) != -1 :
        VPgPosition = Seq.find(ivpg)+4
        VPgSequence = ivpg
        VPgCS = Seq[Seq.find(ivpg)+3]+"/"+Seq[Seq.find(ivpg)+4]

for inia in LibNIa: 
    if  Seq.find(inia) != -1 :
        NIaPosition = Seq.find(inia)+4
        NIaSequence = inia
        NIaCS = Seq[Seq.find(inia)+3]+"/"+Seq[Seq.find(inia)+4]

for inib in LibNIb: 
    if  Seq.find(inib) != -1 :
        NIbPosition = Seq.find(inib)+6
        NIbSequence = inib
        NIbCS = Seq[Seq.find(inib)+5]+"/"+Seq[Seq.find(inib)+6]


#Detecting the Positions and Sequences of Proteins
SequenceP1 = Seq[0:P1Position]
PositionP1 = "1 - "+str(P1Position)

SequenceHCPro = Seq[P1Position:HCProPosition]
PositionHCPro = str(P1Position+1)+" - "+str(HCProPosition)

SequenceP3 = Seq[HCProPosition:P3Position]
PositionP3 = str(HCProPosition+1)+" - "+str(P3Position)

Sequence6K1 = Seq[P3Position:SixK1Position]
Position6K1 = str(P3Position+1)+" - "+str(SixK1Position)

SequenceCI = Seq[SixK1Position:CIPosition]
PositionCI = str(SixK1Position+1)+" - "+str(CIPosition)

Sequence6K2 = Seq[CIPosition:SixK2Position]
Position6K2 = str(CIPosition+1)+" - "+str(SixK2Position)

SequenceVPg = Seq[SixK2Position:VPgPosition]
PositionVPg = str(SixK2Position+1)+" - "+str(VPgPosition)

SequenceNIa = Seq[VPgPosition:NIaPosition]
PositionNIa = str(VPgPosition+1)+" - "+str(NIaPosition)

SequenceNIb = Seq[NIaPosition:NIbPosition]
PositionNIb = str(NIaPosition+1)+" - "+str(NIbPosition)

SequenceCP = Seq[NIbPosition:]
PositionCP = str(NIbPosition+1)+" - "+str(len(Seq))



htmls = htmls.replace("SequName",SeqName)

#SVG Editor
htmls = htmls.replace("P1CS",P1CS)
htmls = htmls.replace("P1PoX",str(P1Position))
htmls = htmls.replace("HCProCS",HCProCS)
htmls = htmls.replace("HCProPoX",str(HCProPosition))
htmls = htmls.replace("P3CS",P3CS)
htmls = htmls.replace("P3PoX",str(P3Position))
htmls = htmls.replace("6K1CS",SixK1CS)
htmls = htmls.replace("6K1PoX",str(SixK1Position))
htmls = htmls.replace("CICS",CICS)
htmls = htmls.replace("CIPoX",str(CIPosition))
htmls = htmls.replace("6K2CS",SixK2CS)
htmls = htmls.replace("6K2PoX",str(SixK2Position))
htmls = htmls.replace("VPgCS",VPgCS)
htmls = htmls.replace("VPgPoX",str(VPgPosition))
htmls = htmls.replace("NIaCS",NIaCS)
htmls = htmls.replace("NIaPoX",str(NIaPosition))
htmls = htmls.replace("NIbCS",NIbCS)
htmls = htmls.replace("NIbPoX",str(NIaPosition))

#Table Editor
htmls = htmls.replace("P1SeqReng",PositionP1)
htmls = htmls.replace("P1ClSi",P1CS)
htmls = htmls.replace("P1ClPo",str(P1Position))
htmls = htmls.replace("HCProSeqReng",PositionHCPro)
htmls = htmls.replace("HCProClSi",HCProCS)
htmls = htmls.replace("HCProClPo",str(HCProPosition))
htmls = htmls.replace("P3SeqReng",PositionP3)
htmls = htmls.replace("P3ClSi",P3CS)
htmls = htmls.replace("P3ClPo",str(P3Position))
htmls = htmls.replace("6K1SeqReng",Position6K1)
htmls = htmls.replace("6K1ClSi",SixK1CS)
htmls = htmls.replace("6K1ClPo",str(SixK1Position))
htmls = htmls.replace("CISeqReng",PositionCI)
htmls = htmls.replace("CIClSi",CICS)
htmls = htmls.replace("CIClPo",str(CIPosition))
htmls = htmls.replace("6K2SeqReng",Position6K2)
htmls = htmls.replace("6K2ClSi",SixK2CS)
htmls = htmls.replace("6K2ClPo",str(SixK2Position))
htmls = htmls.replace("VPgSeqReng",PositionVPg)
htmls = htmls.replace("VPgClSi",VPgCS)
htmls = htmls.replace("VPgClPo",str(VPgPosition))
htmls = htmls.replace("NIaSeqReng",PositionNIa)
htmls = htmls.replace("NIaClSi",NIaCS)
htmls = htmls.replace("NIaClPo",str(NIaPosition))
htmls = htmls.replace("NIbSeqReng",PositionNIb)
htmls = htmls.replace("NIbClSi",NIbCS)
htmls = htmls.replace("NIbClPo",str(NIbPosition))
htmls = htmls.replace("CPSeqReng",PositionCP)

#HTML Generatore
WriteFileName = open("index.html","w")
WriteFileName.write(htmls)
WriteFileName.close


if platform.system()=="Linux" or platform.system()=="Windows":
    webbrowser.open_new_tab('index.html')
else:
    A=input("Please Use Linux.")
