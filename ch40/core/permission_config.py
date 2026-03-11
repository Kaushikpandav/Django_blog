from product.models import Product


PERMISSION_CONFIG = {
  "seller": {
    Product: ["view", "add", "change", "delete"],
    # order: ["view", "create", "change", "delete"],
  },
  "customer": {
    Product:["view", "add"],
  }
}