import DashboardLayout from "@/pages/Layout/DashboardLayout.vue";

import KGFields from "@/pages/KnowledgeGraph/Fields.vue";
import KGFieldDetails from "@/pages/KnowledgeGraph/FieldDetails.vue";
import PersonalDetails from "@/pages/KnowledgeGraph/PersonalDetails.vue";
import NodeFeeds from "@/pages/NodeFeeds.vue";
// import Dashboard from "@/pages/Dashboard.vue";
// import Icons from "@/pages/Icons.vue";
// import Notifications from "@/pages/Notifications.vue";
import UserProfile from "@/pages/UserProfile.vue";
// import TableList from "@/pages/TableList.vue";
// import Typography from "@/pages/Typography.vue";

const routes = [
  {
    path: "/",
    component: DashboardLayout,
    redirect: "knowledgegraph/fields",
    children: [
      {
        path: "knowledgegraph/fields",
        name: "Knowledge Graph - Fields",
        component: KGFields
      },
      {
        path: "knowledgegraph/fields/:field",
        name: "Knowledge Graph - Field Details",
        component: KGFieldDetails
      },
      {
        path: "knowledgegraph/person/:name",
        name: "Personal Details",
        component: PersonalDetails
      },
      {
        path: "nodefeeds",
        name: "Node Feeds",
        component: NodeFeeds
      },
      // {
      //   path: "dashboard",
      //   name: "Dashboard",
      //   component: Dashboard
      // },
      // {
      //   path: "icons",
      //   name: "Icons",
      //   component: Icons
      // },
      // {
      //   path: "notifications",
      //   name: "Notifications",
      //   component: Notifications
      // },
      {
        path: "user",
        name: "User Profile",
        component: UserProfile
      }
      // {
      //   path: "table",
      //   name: "Table List",
      //   component: TableList
      // },
      // {
      //   path: "typography",
      //   name: "Typography",
      //   component: Typography
      // }
    ]
  }
];

export default routes;
