$(function () {
    $('body').append(`
        <div class="galleryShadow"></div>
        <div class="galleryModal">
          <i class="galleryIcon gIquit fa fa-times-circle"></i>
          <i class="galleryIcon gIleft fa fa-chevron-left"></i>
          <i class="galleryIcon gIright fa fa-chevron-right"></i>
          <div class="galleryContainer">
              <img src="">
          </div>  
        </div>
        `)
    $(document).on("click",".gIquit", function (e) {
        $('.galleryModal').css({ 'transform': 'scale(0)' })
        $('.galleryShadow').fadeOut()
    })
    $(document).on("click", ".galleryItem", ".gallery", function (e) {
        galleryNavigate($(this), 'opened')
        $('.galleryModal').css({ 'transform': 'scale(1)' })
        $('.galleryShadow').fadeIn()
    })
    let galleryNav
    let galleryNew
    let galleryNewImg
    let galleryNewText
    $(document).on("click", ".gIleft", function (e) {
        galleryNew = $(galleryNav).prev()
        galleryNavigate(galleryNew, 'last')
    })
    $(document).on("click", ".gIright", function (e) {
        galleryNew = $(galleryNav).next()
        galleryNavigate(galleryNew, 'first')
    })
    function galleryNavigate(gData, direction) {
        galleryNewImg = gData.children('img').attr('src')
        if (typeof galleryNewImg !== "undefined") {
            galleryNav = gData
            $('.galleryModal img').attr('src', galleryNewImg)
        }
        else {
            gData = $('.galleryItem:' + direction)
            galleryNav = gData
            galleryNewImg = gData.children('img').attr('src')
            $('.galleryModal img').attr('src', galleryNewImg)
        }
        galleryNewText = gData.children('img').attr('data-text')
        if (typeof galleryNewText !== "undefined") {
            $('.galleryModal .galleryContainer .galleryText').remove()
            $('.galleryModal .galleryContainer').append('<div class="galleryText">' + galleryNewText + '</div>')
        }
        else {
            $('.galleryModal .galleryContainer .galleryText').remove()
        }
    }
})