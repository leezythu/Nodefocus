<template>
  <div>
    <d3-network
      :net-nodes="graphData.nodes"
      :net-links="graphData.links"
      :options="propOptions"
      :nodeCb="nodeCb"
      :customForces="graphData.customForces"
      :selection="{
        nodes: graphData.selected.nodes,
        links: graphData.selected.links
      }"
      @node-click="nodeClick"
    />
  </div>
</template>
<script>
import D3Network from "vue-d3-network";
import { getNodeColor } from "./nodeColors";
export default {
  name: "D3Net",
  components: {
    D3Network
  },
  props: {
    netdata: {
      type: Object
    },
    propOptions: {
      type: Object
    },
    selectionChange: {
      type: Object
    }
  },
  data() {
    return {
      windowsize: {
        w: Number,
        h: Number
      },
      maxNodeSize: Number,
      graphData: {
        nodes: [],
        links: [],
        selected: {
          nodes: {},
          links: {}
        },
        customForces: {
          Collide: [
            function(d) {
              return d._size / 2;
            }
          ]
        }
      }
    };
  },
  watch: {
    netdata: function(newData) {
      this.graphData.nodes = newData.nodes;
      this.graphData.links = newData.links;
      for (var i = 0; i < this.graphData.nodes.length; i++) {
        var ratio =
          Math.ceil((newData.nodes[i]._size / newData.largestNodeSize) * 10) /
          10;
        // change the node color into actual color;
        this.graphData.nodes[i]._color = getNodeColor(
          newData.nodes[i]._color,
          ratio,
          newData.isFieldDetails,
          newData.isPersonalDetails
        );
        // change the node size into percentage and multiply with the window size friendly node size;
        this.graphData.nodes[i]._size = ratio * this.maxNodeSize;
        this.graphData.nodes[i].size = this.graphData.nodes[i]._size;
      }
      this.setNodeSize();
      if (newData.isPersonalDetails) {
        this.resizeHandler();
      }
    },
    selectionChange: function(newSelectionNode) {
      var node = this.graphData.nodes.find(x => x.id == newSelectionNode.id);
      if (newSelectionNode.nodeSelected) {
        this.selectNode(node);
      } else {
        this.unSelectNode(node.id);
      }
      this.selectNodesLinks();
    }
  },
  created() {
    this.reset();
    window.addEventListener("resize", this.resizeHandler);
    this.resizeHandler();
  },
  destroyed() {
    window.removeEventListener("resize", this.resizeHandler);
  },
  computed: {
    showSel() {
      return true;
    }
  },
  methods: {
    reset() {
      this.graphData.selected.nodes = {};
      this.graphData.selected.links = {};
    },
    nodeCb(node) {
      node._size = node.size * this.propOptions.sizeRatio;
      return node;
    },
    getMaxNodeSize() {
      return Math.floor(
        Math.sqrt(
          Math.pow(this.windowsize.w * 0.2, 2) +
            Math.pow(this.windowsize.h * 0.2, 2)
        )
      );
    },
    setNodeSize() {
      var newMaxNodeSize = this.getMaxNodeSize();
      for (var i = 0; i < this.graphData.nodes.length; i++) {
        this.graphData.nodes[i].size = Math.floor(
          (this.graphData.nodes[i].size * newMaxNodeSize) / this.maxNodeSize
        );
        this.graphData.nodes[i]._size =
          this.graphData.nodes[i].size * this.propOptions.sizeRatio; // store the default size into "size"
      }
      this.maxNodeSize = newMaxNodeSize;
    },
    resizeHandler() {
      this.windowsize.w = new Number(
        Math.max(document.documentElement.clientWidth, window.innnerWidth || 0)
      );
      this.windowsize.h = new Number(
        Math.max(document.documentElement.clientHeight, window.innerHeight || 0)
      );
      this.propOptions.forces.Y =
        Math.floor(((0.5 * this.windowsize.w) / this.windowsize.h) * 10) / 10;
      this.propOptions.forces.X =
        Math.floor(((0.5 * this.windowsize.h) / this.windowsize.w) * 10) / 10;
      this.setNodeSize();
    },
    nodeClick(event, node) {
      if (this.graphData.selected.nodes[node.id]) {
        this.unSelectNode(node.id);
        // is not selected
      } else {
        this.selectNode(node);
      }
      this.selectNodesLinks();
    },
    selectNode(node) {
      this.graphData.selected.nodes[node.id] = node;
      this.emitSelected(node);
    },
    unSelectNode(nodeId) {
      if (this.graphData.selected.nodes[nodeId]) {
        delete this.graphData.selected.nodes[nodeId];
      }
      this.emitUnselected(nodeId);
      this.selectNodesLinks();
    },
    emitSelected(node) {
      this.$emit("selected", node);
    },
    emitUnselected(nodeId) {
      this.$emit("unselected", nodeId);
    },
    selectLink(link) {
      this.$set(this.graphData.selected.links, link.id, link);
    },
    unSelectLink(linkId) {
      if (this.graphData.selected.links[linkId]) {
        delete this.graphData.selected.links[linkId];
      }
    },
    selectNodesLinks() {
      for (let link of this.graphData.links) {
        // node is selected
        if (
          this.graphData.selected.nodes[link.sid] ||
          this.graphData.selected.nodes[link.tid]
        ) {
          this.selectLink(link);
          // node is not selected
        } else {
          this.unSelectLink(link.id);
        }
      }
    }
  }
};
</script>

<style lang="stylus">
.node
  stroke white
  stoke-width 10px

.link
  stroke lightgrey

.link.selected
  stroke-width 3px
  stroke #42B883

.node.selected
  stroke-width 3px
  stroke black
</style>
