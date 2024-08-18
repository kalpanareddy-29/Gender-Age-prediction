# Gender-Age-prediction
The model is build for Predicting Age and Gender by seeing the person.
PROBLEM STATEMENT:In the context of cinema screenings, especially for horror movies, it is crucial to enforce age restrictions to ensure that the content is appropriate for the audience. Typically, individuals below the age of 13 and above the age of 60 are not allowed entry to such screenings due to the potentially distressing content. However, manual verification of age at movie theatres can be inefficient, prone to human error, and may lead to inaccurate enforcement of these restrictions.

The goal of this project is to develop a deep learning-based model that can accurately predict the age and gender of individuals from facial images captured at cinema entrances. The model will be deployed in a user-friendly interface, allowing theatre staff to quickly and accurately assess whether a patron is within the allowed age range (13 to 60 years old) for horror movie screenings. This solution aims to streamline the age verification process, reduce errors, and ensure compliance with age-related restrictions, enhancing the overall movie-going experience and safety.
I build a model on this and achieving a better accuracy of 75% ont his model after tuning the paramenters.

![image](https://github.com/user-attachments/assets/aed2a4f5-e56b-47be-b729-83c2cefbe6ca)
Model: "functional_8"
┏━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┓
┃ Layer (type)        ┃ Output Shape      ┃    Param # ┃ Connected to      ┃
┡━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━┩
│ input_layer_1       │ (None, 48, 48, 3) │          0 │ -                 │
│ (InputLayer)        │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ conv2d_2 (Conv2D)   │ (None, 46, 46,    │        896 │ input_layer_1[0]… │
│                     │ 32)               │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ max_pooling2d_2     │ (None, 23, 23,    │          0 │ conv2d_2[0][0]    │
│ (MaxPooling2D)      │ 32)               │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ conv2d_3 (Conv2D)   │ (None, 21, 21,    │     18,496 │ max_pooling2d_2[… │
│                     │ 64)               │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ max_pooling2d_3     │ (None, 10, 10,    │          0 │ conv2d_3[0][0]    │
│ (MaxPooling2D)      │ 64)               │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ flatten_1 (Flatten) │ (None, 6400)      │          0 │ max_pooling2d_3[… │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ dense_2 (Dense)     │ (None, 128)       │    819,328 │ flatten_1[0][0]   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ dropout_1 (Dropout) │ (None, 128)       │          0 │ dense_2[0][0]     │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ gender_output       │ (None, 2)         │        258 │ dropout_1[0][0]   │
│ (Dense)             │                   │            │                   │
├─────────────────────┼───────────────────┼────────────┼───────────────────┤
│ age_output (Dense)  │ (None, 1)         │        129 │ dropout_1[0][0]   │
└─────────────────────┴───────────────────┴────────────┴───────────────────┘
 Total params: 839,107 (3.20 MB)
 Trainable params: 839,107 (3.20 MB)
 Non-trainable params: 0 (0.00 B)
