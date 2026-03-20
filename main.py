from fastapi import FastAPI, Request  #Request stores all Query and Path params (QUERY PARAMS => ? AGE=18 & NAME=HARSH)
                                                                               #(PATH PARAMS => /1/2/3...)
from Productsdata import products
from datatypes import Structure  
app = FastAPI()                       #Creating Server for Backend



@app.get("/")                         #Creating a Router
def Home():
    return "Welcome to Home page"

@app.get("/Products")
def Products():
    return products

                ######         CRUD OPERATIONS    (use POSTMAN as a client to send data to our backend server in the form of body json structure)         #######

@app.get("/Products/{product_id}")  #Read, PATH PARAMS
def fetch(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/Products/add")     #Create
def add(product:Structure):
    finprod = product.model_dump()
    products.append(finprod)    
    return {"status":"Product Created Successfully!","data":products}

@app.put("/Products/update/{product_id}")   #Update
def update(updproduct:Structure, product_id:int):
    for index,oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products[index] = updproduct.model_dump()
            return {"status":"Product Updated Successfully!","data":products}
    
    return {"error": "Product not found"}
    
@app.delete("/Products/delete/{product_id}")  #Delete
def delete(product_id:int):
    for index,oneProduct in enumerate(products):
        if oneProduct.get("id") == product_id:
            products.remove(oneProduct) #products.pop(index)
            return {"status":"Product Deleted Successfully!","data":products}
        
    return {"error": "Product not found"}