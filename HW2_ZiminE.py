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

        # We extract feature names (columns) and construct a document-term matrix
        columns = []
        for sent in corpus:
            for word in sent.lower().split():
                word = re.sub(r'[!?.,:;\'"$&%_]', '', word)
                if word not in columns:
                    columns.append(word)

        self._feature_names = columns

        indices = list(range(len(corpus)))  # indices for matrix
        dtmatrix = [[0 for column in columns] for index in indices]  # zero-matrix

        # Here is we count the number of occurrences of words in the sentence of corpus \
        # and filling up a zero-matrix
        for i, column in enumerate(columns):
            for index in indices:
                count = 0
                for word in corpus[index].lower().split():
                    word_cleaned = re.sub(r'[!?.,:;\'"$&%_]', '', word)
                    if column == word_cleaned:
                        count += 1
                dtmatrix[index][i] += count
        return dtmatrix

    def get_feature_names(self):
        """Extract feature names (tokens)"""
        return self._feature_names


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
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
