import re  # For dealing with punctuation marks
import pandas as pd  # For better tables representation

class CountVectorizer:

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
        
        # Here we lower all words in corpus and eliminate punctuation marks
        corpus = [list(map(lambda x: re.sub(r'[!?.,:;\'"$&%_]', '', x.lower()), sent.split())) for sent in corpus]
        columns = list(set(sum(corpus, [])))    # save one duplicate of each word in corpus

        self._feature_names = columns

        # Here is we count the number of occurrences of words in the sentence of corpus \
        # and filling up a zero-matrix
        
        rows = range(len(corpus))
        dtmatrix = np.zeros((len(rows), len(columns))).astype(int)   # create zero-matrix and then fill up it
        for i, column in enumerate(columns):
            for j in rows:
                dtmatrix[j][i] = corpus[j].count(column)
        return dtmatrix

    def get_feature_names(self):
        """Extract feature names (tokens)"""
        return self._feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta! !again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)


    # More convenient representation using pandas
    pd.set_option('display.max_columns', None)
    df = pd.DataFrame(count_matrix, columns=vectorizer.get_feature_names())
    print(df)
