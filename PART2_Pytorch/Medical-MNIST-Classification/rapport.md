# Rapport : 

Nous utilisons un modèle de CNN. Le jeux de données provient de données médicales issues de différentes sources (TCIA, RSNA et NIH). Elles ont été travaillées pour les rendre compatibles en ajustant leur taille afin d'obtenir un ensemle cohérent et comparable.


## I_Paramètres Originaux : 

```
    learnRate = 0.01        # Define a learning rate.
    maxEpochs = 20          # Maximum training epochs
    t2vRatio = 1.2          # Maximum allowed ratio of validation to training loss
    t2vEpochs = 3           # Number of consecutive epochs before halting if validation loss exceeds above limit
    batchSize = 300         # Batch size. Going too large will cause an out-of-memory error.

```


**epochs**

```
    Epoch =   0; Training loss = 0.8207; Validation loss = 0.2085
    Epoch =   1; Training loss = 0.1681; Validation loss = 0.1236
    Epoch =   2; Training loss = 0.1049; Validation loss = 0.0819
    Epoch =   3; Training loss = 0.0694; Validation loss = 0.0576
    Epoch =   4; Training loss = 0.0502; Validation loss = 0.0455
    Epoch =   5; Training loss = 0.0389; Validation loss = 0.0398
    Epoch =   6; Training loss = 0.0319; Validation loss = 0.0305
    Epoch =   7; Training loss = 0.0266; Validation loss = 0.0259
    Epoch =   8; Training loss = 0.0226; Validation loss = 0.0227
    Epoch =   9; Training loss = 0.0197; Validation loss = 0.0210
    Epoch =  10; Training loss = 0.0173; Validation loss = 0.0196
    Epoch =  11; Training loss = 0.0153; Validation loss = 0.0173
    Epoch =  12; Training loss = 0.0134; Validation loss = 0.0155
    Epoch =  13; Training loss = 0.0124; Validation loss = 0.0131
    Epoch =  14; Training loss = 0.0110; Validation loss = 0.0133
    Epoch =  15; Training loss = 0.0100; Validation loss = 0.0139
    Epoch =  16; Training loss = 0.0092; Validation loss = 0.0120
    Validation loss too high; halting to prevent overfitting

```

On note une légère tendance à l'overfitting à la fin de l'apprentissage (epochs 14 à 16). La validation loss ré-augmente progressivement, tandis que la la training loss continue de diminuer.

**confusion matrix**

```
    Correct predictions:  5712 of 5740
    Confusion Matrix:
    [[966   0   6   0   0   0]
    [  0 898   0   0   0   0]
    [  3   1 988   0   0   0]
    [  0   0   0 957   5   1]
    [  0   1   0   2 930   6]
    [  2   0   0   0   1 973]]
    ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']

```

La class comportant le plus d'erreurs de prédictions est 'ChestCT'.

**accuracy = 99.51219512195122**

**learning_rate**

## II_test sur t2vRatio :

t2vRatio = 1.8

**epochs**

```
    Epoch =   0; Training loss = 0.6016; Validation loss = 0.1977
    Epoch =   1; Training loss = 0.1635; Validation loss = 0.1312
    Epoch =   2; Training loss = 0.1081; Validation loss = 0.0838
    Epoch =   3; Training loss = 0.0730; Validation loss = 0.0612
    Epoch =   4; Training loss = 0.0527; Validation loss = 0.0450
    Epoch =   5; Training loss = 0.1120; Validation loss = 0.0570
    Epoch =   6; Training loss = 0.0428; Validation loss = 0.0367
    Epoch =   7; Training loss = 0.0303; Validation loss = 0.0285
    Epoch =   8; Training loss = 0.0243; Validation loss = 0.0247
    Epoch =   9; Training loss = 0.0204; Validation loss = 0.0215
    Epoch =  10; Training loss = 0.0176; Validation loss = 0.0203
    Epoch =  11; Training loss = 0.0151; Validation loss = 0.0177
    Epoch =  12; Training loss = 0.0132; Validation loss = 0.0182
    Epoch =  13; Training loss = 0.0119; Validation loss = 0.0186
    Epoch =  14; Training loss = 0.0106; Validation loss = 0.0185
    Epoch =  15; Training loss = 0.0095; Validation loss = 0.0138
    Epoch =  16; Training loss = 0.0087; Validation loss = 0.0135
    Epoch =  17; Training loss = 0.0077; Validation loss = 0.0116
    Epoch =  18; Training loss = 0.0070; Validation loss = 0.0112
    Epoch =  19; Training loss = 0.0066; Validation loss = 0.0117

```

À mesure que le nombre d'époques augmente, la Training loss diminue, ce qui indique que le modèle s'améliore dans l'ajustement des données d'entraînement. Cependant, il est important de surveiller également la Validation loss car elle mesure la capacité du modèle à généraliser à de nouvelles données. Si le modèle surajuste les données d'entraînement, la Validation loss commencera à augmenter, ce qui peut être observé à l'époque 5 où il y a une augmentation de la Validation loss.
On ne note cepandant pas de suraprentissage.

**confusion matrix**

```
    Correct predictions:  5719 of 5740
    Confusion Matrix:
    [[968   0   4   0   0   0]
    [  0 898   0   0   0   0]
    [  4   1 987   0   0   0]
    [  0   0   0 958   5   0]
    [  1   0   0   2 935   1]
    [  1   0   1   0   1 973]]
    ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']

```

Dans ce test, les classes les plus mal prédites sont : AbdomenCT et Hand avec 6 mauvaises prédictions dans chaques classes. 

**accuracy = 99.63414634146342**

Ces paramètres augmentent la performance du modèle sans générer d'overfitting. 

## III_Augmenter la taille et le nombre de convolutions

paramètres originaux :

```
    numConvs1 = 5
    convSize1 = 7
    numConvs2 = 10
    convSize2 = 7 

```

test sur de nouveaux paramètres : 

```
    numConvs1 = 6
    convSize1 = 8
    numConvs2 = 10
    convSize2 = 7

```

**epochs**

```
    Epoch =   0; Training loss = 0.7846; Validation loss = 0.2093
    Epoch =   1; Training loss = 0.1629; Validation loss = 0.1243
    Epoch =   2; Training loss = 0.1069; Validation loss = 0.0891
    Epoch =   3; Training loss = 0.0741; Validation loss = 0.0623
    Epoch =   4; Training loss = 0.0542; Validation loss = 0.0459
    Epoch =   5; Training loss = 0.0418; Validation loss = 0.0394
    Epoch =   6; Training loss = 0.0338; Validation loss = 0.0416
    Epoch =   7; Training loss = 0.0291; Validation loss = 0.0282
    Epoch =   8; Training loss = 0.0236; Validation loss = 0.0235
    Epoch =   9; Training loss = 0.0202; Validation loss = 0.0215
    Epoch =  10; Training loss = 0.0175; Validation loss = 0.0218
    Epoch =  11; Training loss = 0.0163; Validation loss = 0.0190
    Epoch =  12; Training loss = 0.0142; Validation loss = 0.0189
    Epoch =  13; Training loss = 0.0125; Validation loss = 0.0227
    Epoch =  14; Training loss = 0.0111; Validation loss = 0.0162
    Epoch =  15; Training loss = 0.0102; Validation loss = 0.0141
    Epoch =  16; Training loss = 0.0093; Validation loss = 0.0149
    Epoch =  17; Training loss = 0.0090; Validation loss = 0.0175
    Epoch =  18; Training loss = 0.0079; Validation loss = 0.0137
    Epoch =  19; Training loss = 0.0084; Validation loss = 0.0140

```


**confusion matrix**

```
    Correct predictions:  5716 of 5740
    Confusion Matrix:
    [[968   0   4   0   0   0]
    [  0 898   0   0   0   0]
    [  3   1 988   0   0   0]
    [  0   0   0 955   7   1]
    [  0   0   0   2 933   4]
    [  0   0   0   0   2 974]]
    ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']

```

**accuracy = 99.58188153310104**

L'accuracy est moins élevée que le précédent score. De plus, on note une tendance à overfiter légérement plus élevée que précédement (epoch 6, epochs 10 à 13, eopchs 16 et 17 puis epoch 19.) Ainsi, nous décidons d'abandonner ce paramètrage. Peut être que réduire la taille et le nombre de convolutions serait une meilleure piste? 
9 élèments ont été classifiés en main à tors, on peut donc penser que cette configuration de modèle ne convient pas pour cette classe. 

## IV_Diminuer la taille des convolutions

paramètres originaux :

```
    numConvs1 = 5
    convSize1 = 7
    numConvs2 = 10
    convSize2 = 7 

```

test sur de nouveaux paramètres : 

```
    numConvs1 = 5
    convSize1 = 7
    numConvs2 = 10
    convSize2 = 5

```

**epochs**

```
    Epoch =   0; Training loss = 0.7543; Validation loss = 0.2177
    Epoch =   1; Training loss = 0.1739; Validation loss = 0.1319
    Epoch =   2; Training loss = 0.1167; Validation loss = 0.0932
    Epoch =   3; Training loss = 0.0819; Validation loss = 0.0653
    Epoch =   4; Training loss = 0.0585; Validation loss = 0.0499
    Epoch =   5; Training loss = 0.0434; Validation loss = 0.0394
    Epoch =   6; Training loss = 0.0341; Validation loss = 0.0322
    Epoch =   7; Training loss = 0.0283; Validation loss = 0.0272
    Epoch =   8; Training loss = 0.0234; Validation loss = 0.0241
    Epoch =   9; Training loss = 0.0201; Validation loss = 0.0213
    Epoch =  10; Training loss = 0.0175; Validation loss = 0.0184
    Epoch =  11; Training loss = 0.0152; Validation loss = 0.0168
    Epoch =  12; Training loss = 0.0137; Validation loss = 0.0156
    Epoch =  13; Training loss = 0.0126; Validation loss = 0.0156
    Epoch =  14; Training loss = 0.0111; Validation loss = 0.0147
    Epoch =  15; Training loss = 0.0102; Validation loss = 0.0131
    Epoch =  16; Training loss = 0.0090; Validation loss = 0.0115
    Epoch =  17; Training loss = 0.0086; Validation loss = 0.0140
    Epoch =  18; Training loss = 0.0077; Validation loss = 0.0116
    Epoch =  19; Training loss = 0.0072; Validation loss = 0.0112

```


**confusion matrix**

```
    Correct predictions:  5722 of 5740
    Confusion Matrix:
    [[969   0   3   0   0   0]
    [  0 898   0   0   0   0]
    [  2   1 989   0   0   0]
    [  0   0   0 959   3   1]
    [  0   0   0   2 934   3]
    [  1   0   1   0   1 973]]
    ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']

```

**accuracy = 99.68641114982579**

C'est avec ce modèle que l'on a obtenu la meilleure accuracy. On note aussi que c'est avec celui-ci que l'on a le moins d'erreurs par classes, celles-ci sont de plus équitablement réparties. 
Il n'y a pas de tendance à l'overfiting (ou vraiment très peu, cf epoch 17.) Nous décidons de concerver ce modèle et de voir si on ne peut encore l'améliorer. 

## V_Ajouter une couche dense 

paramètres originaux :

```
    fcSize1 = 400
    fcSize2 = 80

```

test sur de nouveaux paramètres 

```

    fcSize1 = 400
    fcSize2 = 80
    fcSize3 = 60

```

**epochs** 

```
    Epoch =   0; Training loss = 1.1702; Validation loss = 0.3681
    Epoch =   1; Training loss = 0.2560; Validation loss = 0.1805
    Epoch =   2; Training loss = 0.1522; Validation loss = 0.1189
    Epoch =   3; Training loss = 0.1010; Validation loss = 0.0798
    Epoch =   4; Training loss = 0.0707; Validation loss = 0.0626
    Epoch =   5; Training loss = 0.0527; Validation loss = 0.0483
    Epoch =   6; Training loss = 0.0420; Validation loss = 0.0364
    Epoch =   7; Training loss = 0.0338; Validation loss = 0.0321
    Epoch =   8; Training loss = 0.0284; Validation loss = 0.0290
    Epoch =   9; Training loss = 0.0241; Validation loss = 0.0252
    Epoch =  10; Training loss = 0.0214; Validation loss = 0.0241
    Epoch =  11; Training loss = 0.0183; Validation loss = 0.0180
    Epoch =  12; Training loss = 0.0170; Validation loss = 0.0178
    Epoch =  13; Training loss = 0.0152; Validation loss = 0.0171
    Epoch =  14; Training loss = 0.0139; Validation loss = 0.0149
    Epoch =  15; Training loss = 0.0339; Validation loss = 0.0165
    Epoch =  16; Training loss = 0.0128; Validation loss = 0.0147
    Epoch =  17; Training loss = 0.0106; Validation loss = 0.0147
    Epoch =  18; Training loss = 0.0098; Validation loss = 0.0120
    Epoch =  19; Training loss = 0.0090; Validation loss = 0.0116

```

**confusion matrix**

```
    Correct predictions:  5713 of 5740
    Confusion Matrix:
    [[970   0   2   0   0   0]
    [  0 898   0   0   0   0]
    [  5   2 985   0   0   0]
    [  0   0   0 955   7   1]
    [  0   1   0   2 932   4]
    [  1   0   1   0   1 973]]
    ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']

```

**accuracy = 99.52961672473867**

L'accuracy est moins élevée qu'avec les paramètres précédents, par conséquent, nous décidons de ne pas garder ces paramètres. On note de l'overfiting sur les dernières epochs. Il y a 7 CXR qui ont été classés en main, c'ets beaucoup. 

## VI_Augmenter la taille des couches denses 

Paramètres originaux 

```
    fcSize1 = 400
    fcSize2 = 80

```

Paramètres de test

```
    fcSize1 = 600
    fcSize2 = 100

```

**epochs** 

```
    Epoch =   0; Training loss = 0.8573; Validation loss = 0.2208
    Epoch =   1; Training loss = 0.1714; Validation loss = 0.1277
    Epoch =   2; Training loss = 0.1046; Validation loss = 0.0790
    Epoch =   3; Training loss = 0.0669; Validation loss = 0.0535
    Epoch =   4; Training loss = 0.0473; Validation loss = 0.0421
    Epoch =   5; Training loss = 0.0358; Validation loss = 0.0327
    Epoch =   6; Training loss = 0.0286; Validation loss = 0.0260
    Epoch =   7; Training loss = 0.0238; Validation loss = 0.0248
    Epoch =   8; Training loss = 0.0198; Validation loss = 0.0214
    Epoch =   9; Training loss = 0.0173; Validation loss = 0.0183
    Epoch =  10; Training loss = 0.0151; Validation loss = 0.0171
    Epoch =  11; Training loss = 0.0131; Validation loss = 0.0158
    Epoch =  12; Training loss = 0.0119; Validation loss = 0.0146
    Epoch =  13; Training loss = 0.0107; Validation loss = 0.0130
    Epoch =  14; Training loss = 0.0096; Validation loss = 0.0128
    Epoch =  15; Training loss = 0.0090; Validation loss = 0.0151
    Epoch =  16; Training loss = 0.0080; Validation loss = 0.0123
    Epoch =  17; Training loss = 0.0075; Validation loss = 0.0111
    Epoch =  18; Training loss = 0.0068; Validation loss = 0.0120
    Epoch =  19; Training loss = 0.0065; Validation loss = 0.0103

```

**confusion matrix**

```
    Correct predictions:  5718 of 5740
    Confusion Matrix:
    [[968   0   4   0   0   0]
    [  0 897   1   0   0   0]
    [  1   1 990   0   0   0]
    [  0   0   0 958   4   1]
    [  0   0   0   2 933   4]
    [  1   0   1   0   2 972]]
    ['AbdomenCT', 'BreastMRI', 'ChestCT', 'CXR', 'Hand', 'HeadCT']

```

**accuracy = 99.61672473867596**

L'accuracy est moins élevée que précédement, néamoins, elle se rapproche de nos paramètres les plus performants. Il n'y a pas réellement d'overfitting. On note cependant un certain déséquilibre dans les erreurs de labelisation par classes. 
Nous écartons ce paramètre pour le moment et y reviendrons peut être après avoir optimisés d'autres paramètres. 


## Conclusion 
L'optimisation la plus efficace est donc :

```

    t2vRatio = 1.8

    numConvs1 = 5
    convSize1 = 7
    numConvs2 = 10
    convSize2 = 5

```
