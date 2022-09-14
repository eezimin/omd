import re                       # For dealing with punctuation marks
import pandas as pd             # For better tables representation

class CountVectorizer:

    def __init__(self):
        """Initialization of Count Vectorizer"""

    def fit_transform(self, corpus: list[str]) -> list[list[int]]:
        """
        Create a document-term matrix based on a collection of sentences (corpus).

        Parameters
        ----------
        corpus : list of strings
            Represents the collection of sentences.

        Returns
        -------
        list[list[int]]
            A document-term matrix with frequency of words in corpus (int >= 0)
        """

        # We extract feature names (columns) and construct a document-term matrix
        columns = []
        for sent in corpus:
            for word in sent.lower().split():
                if word not in columns:
                    word = re.sub(r'[!?.,]', '', word)
                    columns.append(word)
        # columns = sorted(list(set(word for sent in corpus for word in sent.lower().split())))
        indices = list(range(len(corpus)))
        dtmatrix = [[corpus[index].lower().split().count(column) for column in columns] for index in indices]

        self._feature_names = columns
        return dtmatrix

    def get_feature_names(self):
        """Extract feature names (tokens)"""
        return self._feature_names

if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    corpus_1 = [
        'This is the first document.',
        'This is the second second document.',
        'And the third one.','Is this the first document?',]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(*count_matrix, sep = '\n')

    # More convenient representation using pandas
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(count_matrix, columns = vectorizer.get_feature_names())
    print(df)