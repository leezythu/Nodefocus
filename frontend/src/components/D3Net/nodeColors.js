export function getNodeColor(
  set,
  percentage,
  needPercentageVariance,
  isPersonal
) {
  if (isPersonal) {
    return personalColor[set - 1];
  }
  var delta =
    needPercentageVariance == true
      ? 100 - Math.floor(percentage * 100) - 50
      : 0;
  if (set > Object.keys(color).length - 1) {
    return LightenDarkenColor(color.color_default, delta);
  } else {
    return LightenDarkenColor(color["color_" + set.toString()], delta);
  }
}

const personalColor = ["#e14eca", "#1d8cf8"];

const color = {
  color_1: "#FF85EA", // pink
  color_2: "#FDF200", // yellow
  color_3: "#7B61F8", // purple
  color_4: "#8AF7E4", // mint
  color_5: "#FF8B8B", // orange
  color_6: "#7FFF00", // emerald green
  color_7: "#CE0000", // red
  color_8: "#48ADF1", // blue
  color_default: "#E4E4E4" // white-grey
};

function LightenDarkenColor(col, amt) {
  var usePound = false;

  if (col[0] == "#") {
    col = col.slice(1);
    usePound = true;
  }

  var num = parseInt(col, 16);

  var r = (num >> 16) + amt;

  if (r > 255) r = 255;
  else if (r < 0) r = 0;

  var b = ((num >> 8) & 0x00ff) + amt;

  if (b > 255) b = 255;
  else if (b < 0) b = 0;

  var g = (num & 0x0000ff) + amt;

  if (g > 255) g = 255;
  else if (g < 0) g = 0;

  return (usePound ? "#" : "") + (g | (b << 8) | (r << 16)).toString(16);
}
