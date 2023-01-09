input.onButtonPressed(Button.A, function () {
    basic.showIcon(IconNames.Cow)
    basic.showIcon(IconNames.Giraffe)
    basic.showIcon(IconNames.Diamond)
    basic.showIcon(IconNames.SmallDiamond)
    if (Math.randomBoolean()) {
        basic.showIcon(IconNames.Skull)
    } else {
        basic.showIcon(IconNames.Square)
    }
})
input.onButtonPressed(Button.B, function () {
    basic.showNumber(2 + 3)
})
