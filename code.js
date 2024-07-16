function validarIngreso()
{
    var mPassword = document.getElementById("txtPassword").value;
   if (mPassword == "Pa$$w0rd")
   {
        //alert("Password correcto!!!! BIENVENIDO !!!!!!")
         window.location.replace("main.html");
   }
   else
   {
        alert("Password no valido !!!! intentelo de Nuevo")
   }
}

// EESTA ES OTRA FUNCION PARA CUANDO CAMBIE EL SELECT DE LA MARCA
function precioMarcas()
{
    var elementoSeleccionado = document.getElementById("cmbMarca")
  
    var mPrecio = 0.0;
    switch (elementoSeleccionado.value)
    {
        case "1":
              mPrecio =  7000;

              break;
        case "2":
                mPrecio =  13000;
                break;
        case "3":
              mPrecio =  6000;
              break;
        case "4":
                mPrecio =  5000;
                break;
        case "5":
                    mPrecio =  7000;
                    break;
    }

    document.getElementById("txtPrecio").value = mPrecio;   

}



function eventoExtras()
{
    alert("ingreso")
}