export default {
  nodes: [],
  links: [],
  // showMenu: false,
  // selected: {},
  // showSelection: false,
  // linksSelected: {},
  options: {
    canvas: false,
    size: {
      w: 700,
      h: 700
    },
    force: 50,
    forces:{
      X:0.1,
      Y:0.1,
      ManyBody: true,
      Center: false,
    },
    offset: {
      x: 0,
      y: 0
    },
    nodeSize: 20,
    fontSize: 10,
    linkWidth: 1,
    nodeLabels: true,
    // linkLabels: false,
    // strLinks: true,
    resizeListener: true
  }
}
