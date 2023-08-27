# docker_odoo16

project docker odoo16

## Custom Module(Addon)

### 1. Rds Market

    Rds Market merupakan aplikasi pencatatan sederhana terkait penjualan product

## Build and Run

```
docker-compose up -d
```

## Add Addon(module)

```
docker exec odoo_16 odoo scaffold addon_name /var/lib/odoo/addons/16.0/custom_addons
```

```
sudo chmod -R a+rwx ../docker_odoo16
```

## Update Addon(module)

1. restart server mechine
   ```
   docker-compose up -d
   ```
2. upgrade addon(module)
