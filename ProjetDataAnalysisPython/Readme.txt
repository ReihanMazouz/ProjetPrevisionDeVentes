Prévision de vente d'un article dans un supermarché
Nous disposons d'un dataset nous donnant des informations sur la vente d'un article en grande surface pour chaque jour de l'année de 2016 à 2019.

Les Paramètres dont nous disposons sont : la quantité d'article vendu, le CA produit par la vente de cette article et par la vente de la famille de l'article, le benéfice qui en découle (marge),le chiffre d'affaire total du magasin et enfin la température et l'humidité dans le magasin.

L'objéctif est de pouvoir prédire la quantité d'article vendu pour un jour futur.


Pour atteindre cet objectif nous sommes passée par differentes phases : 

1/ Implémentaiton d'algorithmes sklearn sans l'aspect temporelle avec prise en compte ou non de la vente de la famille de l'article. 
Les résultats ont été plutôt correctes lorsqu'il s'agissait de prévoir la quantité d'article vendu en fournissant les informations sur le jour même mais ce n'est pas une prévision temporelle. C'est l'algorithme présent dans l'api de notre application flask. 
Lorsqu'on ajoute les informations sur la vente de la famille de l'article on obtient de très bons résultats mais l'intéret est encore plus réstreint car on a en partie des informations sur la quantité d'articles vendus dans ce paramètre. 

2/On a ensuite tenté d'utiliser la time series et d'y implémenter des algorithmes d'ia pour obtenir une prévision temporelle. Il a fallu modifier le dataset pour obtenir un "supervised learning dataset". Les résultats sont beaucoup moins exact même si la tendence est généralement suivit (on peut le voir sur les différents graphiques). 