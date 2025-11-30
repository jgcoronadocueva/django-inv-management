# inventory_app/views/suppliers.py
from django.shortcuts import render, redirect
from inventory_app.forms import SupplierForm
from inventory_app.services import supplier_services


def supplier_list(request):
    suppliers = supplier_services.list_suppliers()
    return render(request, "inventory_app/suppliers/list.html", {"suppliers": suppliers})


def supplier_add(request):
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier_services.create_supplier(form.cleaned_data)
            return redirect("supplier_list")
    else:
        form = SupplierForm()

    return render(request, "inventory_app/suppliers/form.html", {"form": form})

def supplier_detail(request, id):
    supplier = supplier_services.get_supplier(id)
    return render(request, "inventory_app/suppliers/detail.html", {"supplier": supplier})

def supplier_edit(request, id):
    supplier = supplier_services.get_supplier(id)

    if request.method == "POST":
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            supplier_services.update_supplier(supplier, form.cleaned_data)
            return redirect("supplier_detail", id=supplier.id)
    else:
        form = SupplierForm(instance=supplier)
    
    return render(request, "inventory_app/suppliers/form.html", {"form":form, "supplier": supplier})
