radio.setGroup(88)
basic.forever(function () {
    radio.sendValue("lighttt", input.lightLevel())
    basic.pause(1000)
})
