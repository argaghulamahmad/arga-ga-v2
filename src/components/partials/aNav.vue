<template>
    <bNavbar class="navbar-expand-lg navbar-dark bg-primary fixed-top" id="sideNav">
        <bNavbarBrand>
      <span id="toggleIcon">
        <i :class="getDirectionIcon"></i>
      </span>
            <span class="d-block d-lg-none" @click="togglerNavbar">
        <svg id="ARGA-logo" style="height: 70px;">
        <g fill="white"
           transform="matrix(3.5735076754915243,0,0,3.5735076754915243,
                      23.42649402848972,-18.588056291988458)">
          <path d="M6.64 18.68 l-1.32 2.64 l-1.36 2.68 l-2.96 0 l8 -16 l5.34 10.68 l-3 0 l-2.34 -4.7 l-2.36 4.7 l0 0 z M15.66 21.34 l1.34 2.66 l-2.98 0 l-1.32 -2.66 l0 0 l2.96 0 z M29.380000000000003 16.34 c-0.62 0.9 -1.4 1.54 -2.34 1.92 l3.28 5.74 l-3.06 0 l-4.64 -8.02 l2.38 0.02 c0.72 0 1.34 -0.26 1.86 -0.78 c0.54 -0.52 0.8 -1.16 0.8 -1.9 c0 -0.72 -0.26 -1.34 -0.8 -1.86 c-0.52 -0.52 -1.14 -0.78 -1.86 -0.78 l-5.34 0 l-0.3 -0.3 l-1.38 -2.38 l7.02 0 c1.46 0 2.72 0.52 3.76 1.56 c1.04 1.06 1.56 2.3 1.56 3.76 c0 1.12 -0.3 2.12 -0.94 3.02 z M43.42 20.86 c0.68 -0.32 1.28 -0.76 1.8 -1.34 l2.66 0.88 c-0.36 0.54 -0.78 1.04 -1.28 1.48 c-0.48 0.44 -1 0.82 -1.58 1.14 c-0.56 0.32 -1.16 0.56 -1.82 0.72 c-0.64 0.18 -1.3 0.26 -2 0.26 c-2.22 0 -4.08 -0.8 -5.64 -2.36 s-2.36 -3.42 -2.36 -5.64 c0 -2.2 0.78 -4.08 2.36 -5.64 c1.54 -1.58 3.42 -2.36 5.64 -2.36 c1.1 0 2.14 0.2 3.12 0.62 c0.96 0.42 1.82 1 2.56 1.74 l-1.92 1.88 c-1.04 -1.04 -2.28 -1.56 -3.76 -1.56 c-1.46 0 -2.72 0.5 -3.78 1.56 c-1.04 1.04 -1.54 2.3 -1.54 3.76 s0.5 2.74 1.54 3.78 s2.32 1.54 3.78 1.54 c0.8 0 1.54 -0.16 2.22 -0.46 z M41.2 17.34 l0 -2.66 l6.68 0 l-2.66 2.66 l-4.02 0 z M57.34 18.68 l-1.32 2.64 l-1.36 2.68 l-2.96 0 l8 -16 l5.34 10.68 l-3 0 l-2.34 -4.7 l-2.36 4.7 l0 0 z M66.36 21.34 l1.34 2.66 l-2.98 0 l-1.32 -2.66 l0 0 l2.96 0 z">
          </path>
        </g>
      </svg>
      </span>
            <span class="d-none d-lg-block">
          <img class="img-fluid img-profile rounded-circle mx-auto mb-2"
               src="https://avatars3.githubusercontent.com/u/19942092?s=460&v=4" alt="">
        </span>
        </bNavbarBrand>
        <bNavbarToggler ref="toggler" type="button" data-toggle="collapse"
                        target="navbarSupportedContent"
                        data-target="#navbarSupportedContent"
                        aria-controls="navbarSupportedContent"
                        aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </bNavbarToggler>
        <bNavbarCollapse class="navbar-collapse" id="navbarSupportedContent">
            <ul class="navbar-nav">
                <li class="nav-item">
                    <router-link class="nav-link js-scroll-trigger"
                                 to="/" tag="li" active-class="active" exact>
                        <a>Home</a>
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link js-scroll-trigger"
                                 to="/experience" tag="li" active-class="active" exact>
                        <a>Experience</a>
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link js-scroll-trigger"
                                 to="/education" tag="li" active-class="active" exact>
                        <a>Education</a>
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link js-scroll-trigger"
                                 to="/projects" tag="li" active-class="active" exact>
                        <a>Projects</a></router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link js-scroll-trigger"
                                 to="/skills" tag="li" active-class="active" exact>
                        <a>Skills</a></router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link js-scroll-trigger"
                                 to="/interests" tag="li" active-class="active" exact><a>Interests</a>
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link js-scroll-trigger"
                                 to="/achievements" tag="li" active-class="active" exact><a>Achievements</a>
                    </router-link>
                </li>
                <li class="nav-item">
                    <router-link class="nav-link js-scroll-trigger"
                                 to="/contact-me" tag="li" active-class="active" exact><a>Contact
                        Me</a>
                    </router-link>
                </li>
            </ul>
        </bNavbarCollapse>
    </bNavbar>
</template>

<script>
    import bNavbar from 'bootstrap-vue/es/components/navbar/navbar';
    import bNavbarCollapse from 'bootstrap-vue/es/components/collapse/collapse';
    import bNavbarToggler from 'bootstrap-vue/es/components/navbar/navbar-toggle';
    import bNavbarBrand from 'bootstrap-vue/es/components/navbar/navbar-brand';

    export default {
        name: 'aNav',
        props: {
            photoUrl: String,
            name: String,
            photoHrefUrl: String,
        },
        data() {
            return {
                isExpand: false,
            };
        },
        components: {
            bNavbar,
            bNavbarCollapse,
            bNavbarToggler,
            bNavbarBrand,
        },
        computed: {
            getDirectionIcon() {
                if (this.isExpand) {
                    return 'fa fa-angle-up';
                }
                return 'fa fa-angle-down';
            },
        },
        methods: {
            togglerNavbar() {
                this.$refs.toggler.$el.click();
                this.isExpand = !this.isExpand;
            },
        },
    };
</script>
