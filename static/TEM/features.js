const d = new Date();
const dias = ["Domingo","Lunes","Martes","Miércoles","Jueves","Viernes","Sábado"];
const meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Augosto","Septiembre","Octubre","Noviembre","Deciembre"];

function fechaActual() {
    let dia = dias[d.getDay()];
    let mes = meses[d.getMonth()];
    let ano = d.getFullYear();
    let fecha = d.getDate();
    let horas = d.getHours();
    let minutos = d.getMinutes();

    return dia+" "+fecha+" de "+mes+" de "+ano+" - "+horas+":"+minutos
}
document.getElementById("fechaHora").innerHTML = fechaActual();
setInterval('fechaActual()',1000);
