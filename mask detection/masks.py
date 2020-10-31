def mask(path):
  from keras.preprocessing.image import load_img, img_to_array 
  from keras.models import load_model
  import PIL

  img = load_img(path)
  img = img.resize((128, 128))
  img = img_to_array(img) 

  img = img.reshape( -1,128, 128,3)

  model = load_model('model.h5')
  abc = model.predict(img)

  prediction = ""

  for i in abc:
    if i == 0:
      prediction = "Mask On"
    if i == 1:
      prediction = "No Mask On"
    else:
      continue

  print(prediction, abc)

mask('nomask1.jpg')
mask('mask2.jpg')
mask('mask1.jpg')
mask('nomask2.jpg')
