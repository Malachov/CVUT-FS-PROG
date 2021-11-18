<template>
  <div>
    <v-app>
      <v-app-bar app>
        <v-toolbar-title class="pl-8">CSV prediction</v-toolbar-title>
        <v-spacer></v-spacer>

        <v-btn icon class="mr-8">
          <v-icon>mdi-help</v-icon>
        </v-btn>
      </v-app-bar>

      <v-main>
        <v-row class="mt-16 d-flex justify-center text-center">
          <v-col cols="8">
            <Plotly v-if="show_plot" :data="data" :layout="layout"></Plotly>
          </v-col>
        </v-row>
      </v-main>

      <v-footer app>
        <!-- -->
      </v-footer>
    </v-app>
  </div>
</template>

<script>
import { Plotly } from "vue-plotly";

export default {
  components: {
    Plotly,
  },

  data: () => ({
    show_plot: true,
    layout: { showlegend: false },
    data: [],
  }),

  methods: {
    draw_plot(result) {
      let plot_data = [];
      for (var i = 0; i < result.y_axis.length; i++) {
        plot_data.push({
          x: result.x_axis,
          y: result.y_axis[i],
          name: result.names[i],
          line: { width: 1.5 },
        });
      }
      this.data = plot_data;
      console.log(plot_data);
    },
  },

  mounted() {
    window.eel.expose(this.draw_plot, "draw_plot");
  },
};
</script>

<style lang="scss" scoped></style>

