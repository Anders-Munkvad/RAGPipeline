# Retrieval Pipeline

This project implements a semantic search system using a subset of Wikipedia as the knowledge base. Wikipedia articles are embedded using GTE or E5 sentence transformers, then indexed into a FAISS vector store for efficient similarity search. 
Users can input natural language queries and retrieve the most relevant Wikipedia passages based on semantic similarity, not just keyword matching. The code assumes that a Wikipedia dump has been downloaded at https://dumps.wikimedia.org/dawiki/latest/. Preprocessing is then performed on the Wikipedia dump to remove irrelevant content and create a subset of relevant articles from specific categories.

Features:
- Uses either GTE for general-purpose embeddings or E5 for multilingual, high-quality sentence embeddings

- Fast and scalable FAISS vector index for similarity search

- Supports flexible retrieval from Wikipedia-based corpora

- Modular setup for swapping in different embedding models / knowledge bases

Stack:
- FAISS for vector indexing

- GTE / E5 sentence transformers via Hugging Face

- Python for preprocessing and querying

- Subset of Wikipedia dump as the corpus (knowledge base)

Use Cases:
- Semantic question answering

- Information retrieval research

- Multilingual or domain-specific RAG systems

# Example

### Top-5 retrieved chunks for the sample query "Hvem er Harald Blåtand?" (eng. "Who is Harald Blåtand"):

| Rank | Title           | Category |
|------|------------------|----------|
| 1    | Harald Blåtand   | History  |
| 2    | Palnatoke        | History  |
| 3    | Harald Blåtand   | History  |
| 4    | Harald Blåtand   | History  |
| 5    | Harald Blåtand   | History  |

### Retrieval output:

```text
==================================Top document==================================
'''Harald Blåtand''', '''''Harald Gormsson''''', '''''Harald den Gode''''' eller
'''''Harald Gormsen''''' ukendt fødselsår, død senest 987) var søn af kong Gorm
den Gamle og dronning Thyra Dannebod. Han var konge i Danmark fra omkring 958 til
sin død omkring 985. Hans regeringstid blev præget af det spændte forhold til
Danmarks naboer mod syd, dels venderne langs Østersøens sydkyst, dels det tyskromerske
rige, hvis kejser Otto den Store vha. missionærer søgte at indføre
kristendommen i sine nabolande. Harald lod sig kristne tidligt i sin regeringstid
og imødekom anden mulighed er "Den Polske Toke". Navnet er i hvert fald ikke et normalt
nordisk navn. == Harald Blåtands banemand ? == Ifølge en sen overlevering var
han Harald Blåtands banemand og skal have såret ham dødeligt med et pileskud i
bagdelen. Kong Harald stod bøjet, så pilen kom ud af munden på ham.
''Jomsvikingernes saga'' fortæller, at Palnatoke opfostrede Harald Blåtands søn Svend Tveskæg.
Idet Palnatoke ifølge sagaen skulle have været en ivrig tilhænger af den gamle norrøne tro,
modsatte han sig stærkt indførelsen af kristendommen, som Harald Blåtand
- Harald 01 Blåtand Harald 01 Blåtand Kategori:Danskere i 900-tallet Kategori:Personer
fra vikingetiden Kategori:Tjek fødsels- og dødsår Harald 01 Blåtand Kategori:Personer i
Dansk Biografisk Leksikon Kategori:Personer der er konverteret til kristendommen
Jylland, Nonnebakken på Fyn og Trelleborg på Sjælland og Skåne, og hans rige må
have omfattet hele det nuværende Danmark og Skåne. Omkring 985 ragede Harald uklar
med sin søn Svend. Det kom til kamp, og Harald måtte flygte til Jomsborg, hvor han
døde kort efter. == Harald Blåtand og faderen 300px|Den store ] Haralds giftermål med
Tofa kan være indgået netop i 960'erne. Rimeligvis var Harald allerede ved ægteskabets
indgåelse kristen med tanke på både hans svigerfars trosindstilling og fyrstemagt.
Hvad vi ved om Haralds ægteskab med Tofa og tributforhold til
og deres forgængere''; Vikingeskibsmuseet i Roskilde, Gylling, 2020;
* Erik Moltke: ''Runerne i Danmark og deres oprindelse''; Forum, København, 1976;
* Anders W. Mårtensson: "Borgeby" * Anders Olling og Hans Henrik Havsteen:
''Gorm Den Gamle, Harald Blåtand & Svend Tveskæg''; Lindhardt og Ringhof,
2017; == Eksterne henvisninger == * * * * * * * * * * * * * * * .
* * Nationalmuseet - Harald 01 Blåtand Harald 01 Blåtand Kategori:Danskere
==================================Metadata======================================
{'title': 'Harald Blåtand', 'categories': ['History'], 'start_index': 0}
{'title': 'Palnatoke', 'categories': ['History'], 'start_index': 506}
{'title': 'Harald Blåtand', 'categories': ['History'], 'start_index': 11867}
{'title': 'Harald Blåtand', 'categories': ['History'], 'start_index': 999}
{'title': 'Harald Blåtand', 'categories': ['History'], 'start_index': -1}
```
