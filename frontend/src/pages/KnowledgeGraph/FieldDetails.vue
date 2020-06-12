<template>
  <div class="content">
    <card type="knowledgegraph">
      <div id="knowledgegraph" class="knowledgegraph">
        <D3Net
          :netdata="JSON.parse(JSON.stringify(currentGraphData))"
          :propOptions="options"
          :selectionChange="changedSelectionNode"
          @selected="updateSelected"
          @unselected="updateUnselected"
        />
      </div>
    </card>
    <card>
      <div>
        <GraphControlPanel
          :settings="settings"
          :options="options"
          @options="changeOptions"
          @settings="changeSettings"
        />
      </div>
    </card>
    <card>
      <base-table :data="boardData.nodes" :columns="boardData.columns">
        <template slot="columns">
          <th class="text-center">Name</th>
          <th class="text-center">Number of Papers</th>
          <th class="text-center">Action</th>
        </template>
        <template slot-scope="{ row }">
          <td
            v-if="updateSelection"
            :class="getClass(row)"
            @click="toggleSelection(row)"
            class="text-center"
          >
            {{ row.name }}
          </td>
          <td
            v-if="updateSelection"
            :class="getClass(row)"
            @click="toggleSelection(row)"
            class="text-center"
          >
            {{ row.info.paper }}
          </td>
          <td v-if="updateSelection" class="td-actions" :class="getClass(row)">
            <base-button
              class="animation-on-hover"
              type="success"
              size="sm"
              @click="handleClick(row)"
            >
              <i class="tim-icons icon-single-02" /> Profile
            </base-button>
            <base-button
              class="animation-on-hover"
              type="warning"
              size="sm"
              @click="handleAminerClick(row)"
            >
              <i class="tim-icons icon-spaceship" /> Aminer
            </base-button>
          </td>
        </template>
      </base-table>
    </card>
  </div>
</template>
<script>
import { BaseButton, BaseTable, Card } from "@/components/index";
import { getFieldDetails, postCount } from "@/api/api";
import { fieldDetailsOptions } from "./options.js";
import GraphControlPanel from "@/components/D3Net/GraphControlPanel.vue";
import D3Net from "@/components/D3Net/D3Net";

export default {
  name: "KnowledgeGraphFieldDetails",
  components: {
    BaseButton,
    BaseTable,
    Card,
    D3Net,
    GraphControlPanel
  },
  data() {
    return {
      updateSelection: true,
      changedSelectionNode: {},
      fieldName: String,
      graphData: {},
      currentGraphData: {},
      settings: {
        currentNodesLimit: 100,
        maxNodes: 100
      },
      options: fieldDetailsOptions(),
      boardData: {
        columns: ["Name", "Number Of People", "Actions"],
        nodes: []
      }
    };
  },
  created() {
    this.setFieldName();
    this.getFieldDetails(this.$route.params.field, 100); // for testing
  },
  methods: {
    getClass(row) {
      if (row.nodeSelected) {
        return "tableSelected";
      } else {
        return "tableNotSelected";
      }
    },
    responseHandler(obj) {
      for (var i = 0; i < obj.length; i++) {
        var currentTimeData = obj[i];
        var time = currentTimeData.time;
        this.graphData[time] = {};
        this.setFieldColor(currentTimeData.data);
        this.graphData[time]["nodes"] = currentTimeData.data.nodes.sort(
          (a, b) => {
            return a.info.paper < b.info.paper ? 1 : -1;
          }
        );
        this.graphData[time]["links"] = currentTimeData.data.links;
        this.graphData[time]["largestNodeSize"] =
          currentTimeData.data.largestNodeSize;
        this.graphData[time]["isFieldDetails"] = true;
        this.graphData[time]["isPersonalDetails"] = false;
        this.settings.maxNodes = this.graphData[time].largestNodeSize;
      }
    },
    setBoardNodeData() {
      this.boardData.nodes = JSON.parse(
        JSON.stringify(this.currentGraphData.nodes)
      );
      for (let node of this.boardData.nodes) {
        node["nodeSelected"] = false;
      }
    },
    getFieldDetails(query, limit) {
      getFieldDetails(query, limit)
        .then(response => {
          this.responseHandler(response);
          this.currentGraphData = this.graphData["2020-03"];
          this.setBoardNodeData();
        })
        .finally(() => {});
      postCount()
        .then(() => {})
        .finally(() => {});
    },
    handleClick(row) {
      this.$router.push({
        name: "Personal Details",
        params: { name: this.getURLParam(row.name) }
      });
    },
    handleAminerClick(row) {
      // console.log(row);
      window.open(row.link);
    },
    getURLParam(name) {
      return name.replace(" ", "_");
    },
    setFieldName() {
      var tmpList = this.$route.params.field.toString().split("_");
      this.fieldName = tmpList.join(" ");
    },
    setFieldColor(data) {
      let colorIndex;
      switch (this.fieldName) {
        case "Data Mining":
          colorIndex = 1;
          break;
        case "Web Services":
          colorIndex = 2;
          break;
        case "Bayesian Networks":
          colorIndex = 3;
          break;
        case "Web Mining":
          colorIndex = 4;
          break;
        case "Semantic Web":
          colorIndex = 5;
          break;
        case "Machine Learning":
          colorIndex = 6;
          break;
        case "Database Systems":
          colorIndex = 7;
          break;
        case "Information Retrieval":
          colorIndex = 8;
          break;
        default:
          colorIndex = 9;
      }
      for (let i = 0; i < data.nodes.length; i++) {
        data.nodes[i]["_color"] = colorIndex;
      }
    },
    changeOptions(options) {
      this.options = Object.assign({}, options);
    },
    changeSettings(settings) {
      this.settings = Object.assign({}, settings);
      this.getFieldDetails(this.$route.params.field, {
        limit: this.settings.currentNodesLimit
      });
    },
    updateSelected(node) {
      this.updateSelection = false;
      this.boardData.nodes.find(x => x.id == node.id)["nodeSelected"] = true;
      this.updateSelection = true;
    },
    updateUnselected(nodeId) {
      this.updateSelection = false;
      this.boardData.nodes.find(x => x.id == nodeId)["nodeSelected"] = false;
      this.updateSelection = true;
    },
    toggleSelection(row) {
      row.nodeSelected = !row.nodeSelected;
      this.changedSelectionNode = row;
    }
  }
};
</script>
<style></style>
