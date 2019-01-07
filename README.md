# Aws Lambda Layer Warung Pintar

Aws layer adalah fitur dependency untuk AWS Lambda. Jadi intinya di function tidak perlu lagi menaikan dependency yang membuat file function menjadi besar.

Lihat dokumentasi serverless [layers](https://serverless.com/framework/docs/providers/aws/guide/layers/) atau dokumentasi dari aws [layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)

Layers akan mendefine dependency yang kita bikin. Contoh:

```bash
  layers:
    psycopg2: // ini harus sesuai dengan dependency yang digunakan, jika berbeda tidak akan dikenali oleh function kita
      buildScript: ./build.sh
      path: layer
      compatibleRuntimes:
        - python3.7
      allowedAccounts:
        - '*'
```

Tapi perlu diingat, AWS Lambda layer tetap memiliki batasan seperti berikut ini:

>A function can use up to **5 layers** at a time. The total unzipped size of the function and all layers can't exceed the unzipped deployment **package size limit of 250 MB**. For more information, see AWS Lambda Limits.

## Python 3.7

### AWS Lambda layer for psycopg2

To use in your serverless.yml:

```bash
functions:
  hello:
    handler: handler.hello
    layers:
      - arn:aws:lambda:ap-southeast-1:647709804557:layer:psycopg2:1
```

### AWS Lambda layer for requests

To use in your serverless.yml:

```bash
functions:
  hello:
    handler: handler.hello
    layers:
      - arn:aws:lambda:ap-southeast-1:647709804557:layer:requests:1
```