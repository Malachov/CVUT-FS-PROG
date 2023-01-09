

import pandas as pd
from py_pdf_parser.loaders import load_file



document = load_file("Projects\Bergrova\konto.pdf") 

#########################################################################################
#                   Získání sekce s požadovaným obalem z pdf                            #
#########################################################################################

LT=input("Zadejte číslo kontrolovaného obalu:")
LT_end=input("Zadejte číslo následujícího obalu: (Pokud je na konci, zadejte 0)")
#LT="510401"
#LT_end="510402"
#800185

LT_element_start=document.elements.filter_by_text_contains(LT)
LT_element_start=LT_element_start[0]

if LT_end == "0":
    LT_element_end=document.elements[-1]
else:
    LT_element_end=document.elements.filter_by_text_contains(LT_end)
    LT_element_end=LT_element_end[0]

LT_section = document.sectioning.create_section(
    name="cislo obalu",
    start_element=LT_element_start,
    end_element=LT_element_end,
    include_last_element=False,)

#########################################################################################
#                                     Extrakce dat                                      #
#########################################################################################

DL_elements=document.elements.filter_by_text_contains("Bel-Nr").filter_by_section('cislo obalu_0')
DL_elements_mod=DL_elements.filter_by_text_contains("Volkswagen")
#vystřihávání Volkswagenu
if (len(DL_elements_mod)) > 0:
    DL_str=str()
    for x in range(len(DL_elements_mod)):
        DL_str_mod=DL_elements_mod[x].text()
        ind=DL_str_mod.index("------")
        DL_str_mod=DL_str_mod[:ind]
        DL_str += DL_str_mod.lstrip("B-Dat  Abs/Empfae   BEL.    ENTL   Saldo  BA  Bel-Nr    WK-LG-LR   Bemerkung\n") #zkontrolovat, jestli to neuseklo konec
    DL_str += (DL_elements[-1].text().lstrip("B-Dat  Abs/Empfae   BEL.    ENTL   Saldo  BA  Bel-Nr    WK-LG-LR   Bemerkung\n"))
    DL_str = "B-Dat  Abs/Empfae   BEL.    ENTL   Saldo  BA  Bel-Nr    WK-LG-LR   Bemerkung\n" + DL_str
else:
    DL_str=DL_elements.text()
#print(DL_str)
#rozdělení=řádky
DL_list=DL_str.split("\n")
DL_first_line = DL_list[0]
ind=DL_first_line.index("WK-LG-LR")
#rozdělení=sloupce
DL_list_cut=[]
for x in range(len(DL_list)):
    DL_list_line=str(DL_list[x])
    DL_list_line=DL_list_line[:ind]
    DL_list_line=DL_list_line.split()
    DL_list_cut.append(DL_list_line)


#print(DL_list_cut)

    
#########################################################################################
#                   modifikace na č.dílu + ks + datum                                   #
#########################################################################################

for x in ['Abs/Empfae','Saldo','BA']:
    column=DL_list_cut[0].index(x)   
    [x.pop(column) for x in DL_list_cut] 
    
# sečtení BEL. a ENT
DL_list_cut.pop(0)    
for x in range(len(DL_list_cut)): 
    DL_list_cut[x][1]=int(DL_list_cut[x][1])+int(DL_list_cut[x][2])
    DL_list_cut[x].pop(2)

DL_pdf=DL_list_cut
#print(DL_pdf)

#########################################################################################
#                                     import z excelu                                   #
#########################################################################################

df = pd.read_excel("Projects\Bergrova\KT_konto_end.xlsx")

date=df['Unnamed: 0'].values.tolist()
qty=df['Unnamed: 2'].values.tolist()
DL_c=df['Unnamed: 1'].values.tolist()

DL_excel=[]
for x in range(len(date)):
    DL_excel.append([date[x], abs(qty[x]), str(DL_c[x])])
#print(DL_excel)

#########################################################################################
#                                    kontrola                                           #
#########################################################################################
# chybí v jejich
Qty_check_list=[]
for x in range(len(DL_excel)):
    if DL_excel[x][2] in [y[2] for y in DL_pdf]: 
        Qty_check_list.append([[y[1], y[2], DL_excel[x][2], DL_excel[x][1]] for y in DL_pdf if y[2]==DL_excel[x][2]])
        Qty_check_list[x]=Qty_check_list[x][0]
        
        if Qty_check_list[x][0] == Qty_check_list[x][-1]:
            continue
        else:
            print("Neshoda v počtu ks:",Qty_check_list[x],DL_excel[x][0])
        
    else:
        print("V jejich nenalezeno:",DL_excel[x])
        Qty_check_list.append([0,0,0,0])
# chybí v našem
for x in range(len(DL_pdf)):
    if DL_pdf[x][2] in [y[2] for y in DL_excel]: 
        continue
    else:
        print("V našem nenalezeno:",DL_pdf[x])

#print(Qty_check_list)
