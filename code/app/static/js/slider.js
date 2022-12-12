var photos = new Array()
var which = 0

/*Change the below variables to reference your own images. You may have as many images in the slider as you wish*/
photos[0] = "/static/images/1.jpg"
photos[1] = "/static/images/2.jpg"
photos[2] = "/static/images/3.jpg"
photos[3] = "/static/images/4.jpg"

function backward() {
    if (which > 0) {
        window.status = ''
        which--
        document.images.photoslider.src = photos[which]
    }
}

function forward() {
    if (which < photos.length - 1) {
        which++
        document.images.photoslider.src = photos[which]
    }
    else window.status = 'Fin De La Galeria'
}

