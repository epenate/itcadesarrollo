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