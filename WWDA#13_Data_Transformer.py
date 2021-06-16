import pandas as pd
import os
import glob

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

# define a function which read the csv files, count all keywords and their frequency and output it as a csv files


def count_keywords(year):
    df = pd.read_csv(year + ".csv")
    keywords_df = df.keywords.str.split("; ", expand=True)
    keywords_dict = {}
    for list in range(len(keywords_df.values)):
        for value in range(len(keywords_df.values[list])):
            if pd.notnull(keywords_df.values[list][value]):
                keyword = keywords_df.values[list][value]
                if keyword not in keywords_dict:
                    keywords_dict[keyword] = 1
                else:
                    keywords_dict[keyword] = keywords_dict[keyword] + 1
    keywords_freq_df = pd.DataFrame.from_dict(keywords_dict, orient='index')
    keywords_freq_df["year"] = year + "/1/1"
    keywords_freq_df.to_csv(year+'_keywords_freq.csv',
                            index=True, header=False)

# define a function which read the csv files, count all keywords and their number of citations and output it as a csv files


def count_keywords_citations(year):
    df = pd.read_csv(year + ".csv")
    keywords_df = df.keywords.str.split("; ", expand=True)
    df_merged = pd.concat([df, keywords_df], axis=1)
    keywords_citations_dict = {}
    for list in range(len(keywords_df.values)):
        for value in range(len(keywords_df.values[list])):
            if pd.notnull(keywords_df.values[list][value]):
                keyword = keywords_df.values[list][value]
                if keyword not in keywords_citations_dict:
                    keywords_citations_dict[keyword] = df_merged["max_citation"][list]
                else:
                    keywords_citations_dict[keyword] = keywords_citations_dict[keyword] + \
                        df_merged["max_citation"][list]
    keywords_citations_df = pd.DataFrame.from_dict(
        keywords_citations_dict, orient='index')
    keywords_citations_df["year"] = year + "/1/1"
    keywords_citations_df.to_csv(year+'_keywords_citations.csv',
                                 index=True, header=False)


# excute functions for keywords and their frequency
count_keywords("2016")
count_keywords("2017")
count_keywords("2018")
count_keywords("2019")
count_keywords("2020")

# excute functions for keywords and their number of citations
count_keywords_citations("2016")
count_keywords_citations("2017")
count_keywords_citations("2018")
count_keywords_citations("2019")
count_keywords_citations("2020")

# Merge each years' keywords and their number of citations and output as csv file for later data visulisation
all_files = glob.glob(os.path.join(dname, "*_keywords_citations.csv"))
df_from_each_file = (pd.read_csv(f, sep=',', header=None,
                                 names=["keywords", "Number of Citations", "Year"]) for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv("merged_keywords_citations.csv")

# Merge each years' keywords and their frequency and output as csv file for later data visulisation
all_files = glob.glob(os.path.join(dname, "*_keywords_freq.csv"))
df_from_each_file = (pd.read_csv(f, sep=',', header=None,
                                 names=["keywords", "Number of Articles Related", "Year"]) for f in all_files)
df_merged = pd.concat(df_from_each_file, ignore_index=True)
df_merged.to_csv("merged__keywords_freq.csv")
