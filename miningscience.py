# NOMBRE (Pazmiño, Galilea): 

def download_pubmed(keyword):
     Entrez.email = 'galilea.pazmino@est.ikiam.edu.ec'
    handle = Entrez.esearch(db='pubmed',sort='relevance',retmax='500',retmode='xml',term=keyword)
    results = Entrez.read(handle)
    id_list = results["IdList"]
    handle = Entrez.efetch(db='pubmed',
                       retmode='xml',
                       id=id_list)
    return (id_list)
def map_science

with open('mapa.txt',"r", encoding='utf-8-sig') as f:
    my_text = f.read()
    my_text = re.sub(r'\n\s{6}', ' ', my_text)
    text1 = re.findall(r"\,\s[A-Z]+[A-z]{2,11}\.", my_text)
    len(my_text)
    unique_text =list(set(text1))
    unique_text.sort()
    a = unique_text
    print(a[12:17])
    zipcodes = re.findall(r'[A-Z]{2}\s(\d{5}), USA', my_text)
    len(zipcodes)
    zipcodes[5:12]
    unique_zipcodes = list(set(zipcodes))
    unique_zipcodes.sort()
    unique_zipcodes[5:12]
    len(unique_zipcodes)
    zip_coordinates = {}
with open('coordenadas.txt') as f:
    csvr = csv.DictReader(f)
    for row in csvr:
        zip_coordinates[row['ZIP']] = [float(row['LAT']), 
                                       float(row['LNG'])]
        zip_code = []
zip_long = []
zip_lat = []
zip_count = []
for z in unique_zipcodes:
    # if we can find the coordinates
    if z in zip_coordinates.keys():
        zip_code.append(z)
        zip_lat.append(zip_coordinates[z][0])
        zip_long.append(zip_coordinates[z][1])
        zip_count.append(zipcodes.count(z))