<template>
  <div class="content">
    <div class="row">
      <div class="list-group col-6">
        <a
          target="_blank"
          v-for="news in newsLists1"
          :key="news.id"
          :href="news.url"
          class="list-group-item text-left"
        >
          <card>
            <div class="d-flex w-100 justify-content-between ">
              <h5 class="mb-1">
                <b>{{ news.title }}</b>
              </h5>
            </div>
            <small>{{ news.date }}</small>
            <div class="news-content">
              <img :src="news.img" :alt="news.title" />
              <p class="mb-1">
                {{ news.content }}
              </p>
            </div>
            <!-- <small>{{ news.person.toString() }}</small> -->
            <small>{{ formatter(news.fields) }}</small>
          </card>
        </a>
      </div>
      <div class="list-group col-6">
        <a
          v-for="news in newsLists2"
          :key="news.id"
          :href="news.url"
          class="list-group-item text-left"
        >
          <card>
            <div class="d-flex w-100 justify-content-between ">
              <h5 class="mb-1">
                <b>{{ news.title }}</b>
              </h5>
            </div>
            <small>{{ news.date }}</small>
            <div class="news-content">
              <p class="mb-1">
                {{ news.content }}
              </p>
            </div>
            <!-- <small>{{ news.person.toString() }}</small> -->
            <small>{{ formatter(news.fields) }}</small>
          </card>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { Card } from "@/components/index";
import { getNews, postCount } from "@/api/api.js";

export default {
  name: "NodeFeeds",
  components: {
    Card
  },
  data() {
    return {
      newsLists1: [],
      newsLists2: []
    };
  },
  created() {
    this.getNews({});
  },
  methods: {
    formatter(array) {
      let str = array.toString();
      str = str.split(",").join(", ");
      str = str.split("_").join(" ");
      return str;
    },
    responseHandler(response) {
      this.newsLists1 = [];
      this.newsLists2 = [];
      for (let i = 0; i < response.length; i++) {
        response[i].date = response[i].date.split(" ")[0];
        if (i % 2 == 0) {
          this.newsLists1.push(response[i]);
        } else {
          this.newsLists2.push(response[i]);
        }
      }
    },
    getNews(params) {
      getNews(params)
        .then(response => {
          this.responseHandler(response);
        })
        .finally(() => {});
      postCount()
        .then(() => {})
        .finally(() => {});
    }
  }
};
</script>

<style>
.news-content {
  max-height: 300px;
  overflow: scroll;
}
</style>
