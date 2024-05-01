import string


candidate_speech = "K1"

list_of_abscissae=list(string.ascii_uppercase)
list_of_abscissae.remove("I")
abscissa=list_of_abscissae.index(candidate_speech[:1])+1
ordinate=int(candidate_speech[1:])

