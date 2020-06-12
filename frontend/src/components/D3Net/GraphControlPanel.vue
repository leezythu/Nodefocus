<template>
  <div id="menu">
    <div class="row">
      <div class="col-lg-6 col-md-12">
        <card>
          <table class="table">
            <thead>
              <tr>
                <th scope="col" colspan="3">Node & Link</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">
                  Number of Nodes
                </th>
                <td>
                  <input
                    type="range"
                    v-model.number="setts.currentNodesLimit"
                    @input="changeSettings"
                    min="1"
                    :max="setts.maxNodes"
                    step="10"
                  />
                </td>
                <td>
                  <span>{{ setts.currentNodesLimit }}</span>
                </td>
              </tr>
              <tr>
                <th scope="row">
                  Node Size
                </th>
                <td>
                  <input
                    type="range"
                    v-model.number="opts.sizeRatio"
                    @input="change"
                    min="0.1"
                    max="1"
                    step="0.1"
                  />
                </td>
                <td>
                  <span>{{ opts.sizeRatio }}</span>
                </td>
              </tr>
              <tr>
                <th scope="row">
                  Link Thickness
                </th>
                <td>
                  <input
                    type="range"
                    v-model.number="opts.linkWidth"
                    @input="change"
                    min="1"
                    max="15"
                    step="1"
                  />
                </td>
                <td>
                  <span>{{ opts.linkWidth }}</span>
                </td>
              </tr>
              <tr>
                <th scope="row">Font Size</th>
                <td>
                  <input
                    type="range"
                    v-model.number="opts.fontSize"
                    @input="change"
                    min="1"
                    max="30"
                    step="1"
                  />
                </td>
                <td>
                  <span>{{ opts.fontSize }}</span>
                </td>
              </tr>
              <tr>
                <th scope="row">Show node names</th>
                <td>
                  <input
                    type="checkbox"
                    v-model="opts.nodeLabels"
                    @change="change"
                  />
                </td>
                <td></td>
              </tr>
              <tr>
                <th scope="row">Show link names</th>
                <td>
                  <input
                    type="checkbox"
                    v-model="opts.linkLabels"
                    @change="change"
                  />
                </td>
                <td></td>
              </tr>
            </tbody>
          </table>
        </card>
      </div>

      <div class="col-lg-6 col-md-12">
        <card>
          <table class="table">
            <thead>
              <tr>
                <th scope="col" colspan="3">Graph View</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <th scope="row">
                  Force
                </th>
                <td>
                  <input
                    type="range"
                    v-model.number="opts.force"
                    @input="change"
                    min="1"
                    max="5000"
                    step="1"
                  />
                </td>
                <td>
                  <span>{{ opts.force }}</span>
                </td>
              </tr>
              <tr>
                <th scope="row">
                  Force X
                </th>
                <td>
                  <input
                    type="range"
                    v-model.number="opts.forces.X"
                    @input="change"
                    min="0.1"
                    max="1"
                    step="0.1"
                  />
                </td>
                <td>
                  <span>{{ opts.forces.X }}</span>
                </td>
              </tr>
              <tr>
                <th scope="row">
                  Force Y
                </th>
                <td>
                  <input
                    type="range"
                    v-model.number="opts.forces.Y"
                    @input="change"
                    min="0.1"
                    max="1"
                    step="0.1"
                  />
                </td>
                <td>
                  <span>{{ opts.forces.Y }}</span>
                </td>
              </tr>
              <tr>
                <th scope="row">
                  Offset X
                </th>
                <td>
                  <input
                    type="range"
                    v-model.number="opts.offset.x"
                    @input="change"
                    min="-1000"
                    max="1000"
                    step="1"
                  />
                </td>
                <td>
                  <span>{{ opts.offset.x }}</span>
                </td>
              </tr>
              <tr>
                <th scope="row">
                  Offset Y
                </th>
                <td>
                  <input
                    type="range"
                    v-model.number="opts.offset.y"
                    @input="change"
                    min="-1000"
                    max="1000"
                    step="1"
                  />
                </td>
                <td>
                  <span>{{ opts.offset.y }}</span>
                </td>
              </tr>
            </tbody>
          </table>
        </card>
      </div>
    </div>
  </div>
</template>
<script>
import { Card } from "@/components/index";

export default {
  name: "graph-control-panel",
  components: {
    Card
  },
  props: {
    settings: {
      type: Object
    },
    options: {
      type: Object
    }
  },
  data() {
    return {
      opts: {}
    };
  },
  created() {
    this.opts = this.options;
    this.setts = this.settings;
  },
  methods: {
    change() {
      this.$emit("options", this.opts);
    },
    changeSettings() {
      this.$emit("settings", this.setts);
    },
    reset() {
      // this.opts = Object.assign({}, defaultData.options);
      // this.options.width = this.$el.clientWidth;
      // this.options.height = this.$el.clientHeight;
      // this.$emit("reset", this.options);
    },
    emit(e) {
      this.$emit(e);
    }
  }
};
</script>
