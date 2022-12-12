var photos1 = new Array()
var which1 = 0

photos1[0] = "/static/images/5.jpg"
photos1[1] = "/static/images/6.jpg"
photos1[2] = "/static/images/7.jpg"


function backward1() {
    if (which1 > 0) {
        window.status = ''
        which1--
        document.images.photoslider1.src = photos1[which1]
    }
}

function forward1() {
    if (which1 < photos1.length - 1) {
        which1++
        document.images.photoslider1.src = photos1[which1]
    }
    else window.status = 'Fin De La Galeria'
}