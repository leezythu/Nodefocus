export function fieldOptions() {
  return {
    canvas: false,
    force: 1000,
    forces: {
      X: 0.2,
      Y: 0.6,
      ManyBody: true,
      Center: false
    },
    offset: {
      x: 0,
      y: 0
    },
    sizeRatio: 1,
    linkWidth: 1,
    fontSize: 20,
    nodeLabels: true,
    linkLabels: false
  };
}

export function fieldDetailsOptions() {
  return {
    canvas: false,
    force: 750,
    forces: {
      X: 0.5,
      Y: 0.5,
      ManyBody: true,
      Center: false
    },
    offset: {
      x: 0,
      y: 0
    },
    sizeRatio: 0.8,
    linkWidth: 1,
    fontSize: 7,
    nodeLabels: true,
    linkLabels: false
  };
}

export function communityOptions() {
  return {
    size: {
      h: 270
    },
    canvas: false,
    force: 800,
    forces: {
      X: 0.5,
      Y: 0.5,
      ManyBody: true,
      Center: true
    },
    offset: {
      x: 0,
      y: 0
    },
    sizeRatio: 0.05,
    linkWidth: 1,
    fontSize: 8,
    nodeLabels: true,
    linkLabels: true
  };
}

export function personalOptions() {
  return {
    size: {
      h: 270
    },
    canvas: false,
    force: 1000,
    forces: {
      X: 0.5,
      Y: 0.5,
      ManyBody: true,
      Center: true
    },
    offset: {
      x: 0,
      y: 0
    },
    sizeRatio: 0.05,
    linkWidth: 1,
    fontSize: 8,
    nodeLabels: true,
    linkLabels: false
  };
}
