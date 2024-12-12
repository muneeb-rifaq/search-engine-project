# search engine project
 A search engine built using Flask and NextJS 

 The individual functions are made in python and designed to be used by Next JS application 

 The addresses used may have to be adjusted depending on wether computer name is 'AT' or 'hp'.

 1: Initially the program calls function load_dataset in which it pulls from file 'medium_articles.csv' in the 'medium articles' folder (present in downloads)

 2: Next it imports data from that csv file and processes it into chunks so the work can be divided into multiple segments.

 3: The chunk divided content is stored in 'processed_dataset' file to be used by the program later.

 4: Next Program calls clean() function that reads from 'processed_dataset.csv' file and removes stop words and performs lametization and word tokenization

 5: Cleaned data set stored in file  'cleaned_dataset.csv'

 6: Program uses 'cleaned_dataset' to perform create lexicon and store in 'lexicon.csv'

 7: Program uses cleaned_dataset and Lexicon to mak a forward index consisting of a list of words present in every article title.

 8: Program uses forward_index.csv to make backward index consisting of a list of article_titles present for every article word
