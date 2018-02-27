from gensim.models.keyedvectors import KeyedVectors

model = KeyedVectors.load_word2vec_format('bin/GoogleNews-vectors-negative300.bin', binary=True)
information = input('information = ?\n').split()
while(1):
    keyword = input('keyword = ?\n').split()
    distance = model.wmdistance(information, keyword)
    print(distance)
    print()
