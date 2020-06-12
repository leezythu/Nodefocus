<template>
  <div class="content">
    <card type="knowledgegraph">
      <div id="knowledgegraph" class="knowledgegraph">
        <D3Net
          :netdata="JSON.parse(JSON.stringify(currentGraphData))"
          :propOptions="JSON.parse(JSON.stringify(options))"
          :selectionChange="changedSelectionNode"
          @selected="updateSelected"
          @unselected="updateUnselected"
        />
      </div>
    </card>
    <card>
      <base-table
        id="fieldTable"
        class="table-hover"
        :data="boardData.nodes"
        :columns="boardData.columns"
      >
        <template slot="columns">
          <th class="text-center">Fields</th>
          <th class="text-center">Number of People</th>
          <th class="text-center">Action</th>
        </template>
        <template slot-scope="{ row }">
          <td
            v-if="updateSelection"
            :class="getClass(row)"
            @click="toggleSelection(row)"
          >
            {{ row.name }}
          </td>
          <td
            v-if="updateSelection"
            :class="getClass(row)"
            @click="toggleSelection(row)"
          >
            {{ row._size }}
          </td>
          <td
            v-if="updateSelection"
            class="td-actions"
            :class="getClass(row)"
            @click="toggleSelection(row)"
          >
            <base-button type="info" size="sm" icon @click="handleClick(row)">
              <i class="tim-icons icon-tap-02"></i>
            </base-button>
          </td>
        </template>
      </base-table>
    </card>
  </div>
</template>
<script>
import { BaseTable, BaseButton, Card } from "@/components/index";
import { getFields, postCount } from "@/api/api";
import { fieldOptions } from "./options.js";
import D3Net from "@/components/D3Net/D3Net";

export default {
  name: "KnowledgeGraphField",
  components: {
    BaseTable,
    BaseButton,
    Card,
    D3Net
  },
  data() {
    return {
      updateSelection: true,
      changedSelectionNode: {},
      graphData: {},
      currentGraphData: {},
      options: fieldOptions(),
      boardData: {
        columns: ["id", "fields", "Number Of People", "Actions"],
        nodes: []
      }
    };
  },
  created() {
    this.getFields(); // for testing
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
        this.graphData[time]["nodes"] = currentTimeData.data.nodes.sort(
          (a, b) => {
            return a._size < b._size ? 1 : -1;
          }
        );
        this.graphData[time]["links"] = currentTimeData.data.links;
        this.graphData[time]["largestNodeSize"] =
          currentTimeData.data.largestNodeSize;
        this.graphData[time]["isFieldDetails"] = false;
        this.graphData[time]["isPersonalDetails"] = false;
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
    getFields() {
      getFields()
        .then(response => {
          this.responseHandler(response);
          this.currentGraphData = this.graphData["2020"];
          this.setBoardNodeData();
        })
        .finally(() => {});
      postCount()
        .then(() => {})
        .finally(() => {});
    },
    handleClick(row) {
      this.$router.push({
        name: "Knowledge Graph - Field Details",
        params: { field: this.getURLParam(row.name) }
      });
    },
    getURLParam(name) {
      return name.replace(" ", "_");
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
