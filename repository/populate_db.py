import csv
from papers.models import Paper


MAPPING = {
    'author': '\ufeffAuthors',
    'title': 'Title',
    'year': 'Year',
    'source_title': 'Source title',
    'document_type': 'Document Type',
    'abstract': 'Abstract',
    'doi': 'DOI',
}

DICT = {t[1]:t[0] for t in Paper.DOCUMENT_TYPE_OPTIONS}

def dt(row):
    if row == 'Article in Press':
        row = 'Article'
    return DICT[row]


def create_paper(row, labels):
    kwargs = {}
    for field in MAPPING.keys():
        print(field)
        if field == 'document_type':
            val = row[labels.index(MAPPING[field])]
            val = dt(val)
            kwargs[field] = val
        else:
            l = labels.index(MAPPING[field])
            print(l)
            print(len(row))
            kwargs[field] = row[labels.index(MAPPING[field])]
    # print("done")
    Paper(**kwargs).save()



def populate():
    with open('../scopus.csv', newline='', encoding='utf-8') as csvfile:
        papers = csv.reader(csvfile, delimiter=',')
        labels = next(papers)
        print(labels)
        for row in papers:
            create_paper(row, labels)
            print(', '.join(row))

# populate()