# Bibliographie


ℹ️ La bibliographie est dans le format [CSL-JSON](https://github.com/citation-style-language/schema?tab=readme-ov-file#csl-json-schema).

Pour les jeux de données : 

  - L'adresse des fichiers est spécifié par l'attribut `URL`, par exemple

        "URL": "https://archive.ics.uci.edu/static/public/9/data.csv"
 
  - La somme de contrôle associée et l'algorithme utilisé sont fournis
    dans l'attribut personnalisé `checksum`, de la façon suivante :   

        "custom": {
            "checksum": {
                "value": "ca25194200142eb13650f02ec2d64980",
                "type": "md5"
            }
        }