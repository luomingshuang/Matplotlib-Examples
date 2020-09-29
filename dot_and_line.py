import matplotlib.pyplot as plt
acc = history_dict['accuracy'] 
val_acc = history_dict['val_accuracy']
loss = history_dict['loss']
val_loss = history_dict['val_loss']
epochs = range(1, len(acc)+1)
####acc, val_acc, loss, val_loss皆为数组
'''
[0.6222666501998901, 0.7278666496276855, 0.7332666516304016, 0.7689999938011169, 0.7893333435058594, 0.8099333047866821, 0.8284666538238525, 0.8393999934196472, 0.8572666645050049, 0.8683333396911621, 0.8802000284194946, 0.8868666887283325, 0.8925999999046326, 0.8991333246231079, 0.9042666554450989, 0.9092000126838684, 0.9138666391372681, 0.9192666411399841, 0.9208666682243347, 0.9263333082199097, 0.9300666451454163, 0.9335333108901978, 0.9375333189964294, 0.9403333067893982, 0.9439333081245422, 0.9466000199317932, 0.9508000016212463, 0.9528666734695435, 0.9549999833106995, 0.9585333466529846, 0.9604666829109192, 0.9621333479881287, 0.9636666774749756, 0.9662666916847229, 0.966866672039032, 0.9693999886512756, 0.9710666537284851, 0.9718000292778015, 0.9735999703407288, 0.975266695022583]
[0.7114999890327454, 0.7260000109672546, 0.760699987411499, 0.7723000049591064, 0.784500002861023, 0.8043000102043152, 0.8055999875068665, 0.8271999955177307, 0.8403000235557556, 0.8496000170707703, 0.8564000129699707, 0.8639000058174133, 0.8680999875068665, 0.8677999973297119, 0.8705999851226807, 0.8758000135421753, 0.8788999915122986, 0.8790000081062317, 0.8813999891281128, 0.8823000192642212, 0.8828999996185303, 0.8838000297546387, 0.883899986743927, 0.8847000002861023, 0.8848000168800354, 0.8824999928474426, 0.8858000040054321, 0.8845999836921692, 0.8852999806404114, 0.8848000168800354, 0.886900007724762, 0.8848000168800354, 0.8866999745368958, 0.8845999836921692, 0.8851000070571899, 0.8855999708175659, 0.883899986743927, 0.8838000297546387, 0.883899986743927, 0.8833000063896179]
[0.6920461654663086, 0.6872878074645996, 0.6761967539787292, 0.6561088562011719, 0.6251583099365234, 0.5840017795562744, 0.5364459753036499, 0.48869940638542175, 0.443673312664032, 0.40433239936828613, 0.3699362277984619, 0.3413583040237427, 0.31728407740592957, 0.29674068093299866, 0.27869391441345215, 0.2632395625114441, 0.24894070625305176, 0.2361389845609665, 0.22532625496387482, 0.21416525542736053, 0.20510832965373993, 0.19519327580928802, 0.18716655671596527, 0.178892582654953, 0.17165206372737885, 0.16437354683876038, 0.15797266364097595, 0.1512240469455719, 0.1453147530555725, 0.13963383436203003, 0.1345539540052414, 0.128912553191185, 0.12433918565511703, 0.11950121819972992, 0.11579544842243195, 0.11086598038673401, 0.10671283304691315, 0.10280583053827286, 0.098957359790802, 0.09545212984085083]
[0.6904700994491577, 0.6832290291786194, 0.6693345904350281, 0.6458863019943237, 0.6121847033500671, 0.5713838934898376, 0.5269678235054016, 0.48447856307029724, 0.44842857122421265, 0.4155186116695404, 0.38948914408683777, 0.3684239387512207, 0.3519984185695648, 0.3390997648239136, 0.32794275879859924, 0.31814253330230713, 0.310904860496521, 0.3052317500114441, 0.2995576560497284, 0.2956988513469696, 0.2921980619430542, 0.2900373041629791, 0.2879321575164795, 0.28657665848731995, 0.2872593402862549, 0.287251353263855, 0.2847578227519989, 0.28680533170700073, 0.28641778230667114, 0.28724366426467896, 0.28873690962791443, 0.2910003960132599, 0.2912275493144989, 0.2939637005329132, 0.2953062951564789, 0.2981499135494232, 0.3000560402870178, 0.30322638154029846, 0.3055161237716675, 0.30859309434890747]
range(1, 41)
'''
##'bo'代表蓝点
plt.plot(epochs, loss, 'bo', label='Training loss')
##'b'代表蓝色实线
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()