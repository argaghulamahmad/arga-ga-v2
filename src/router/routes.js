/* eslint-disable global-require,import/prefer-default-export */
import aAboutMe from '../components/sections/aAboutMe';

const aAwards = (resolve) => {
  require.ensure(['../components/sections/aAchievements'], () => {
    resolve(require('../components/sections/aAchievements'));
  });
};
const aEducation = (resolve) => {
  require.ensure(['../components/sections/aEducation'], () => {
    resolve(require('../components/sections/aEducation'));
  });
};
const aExperience = (resolve) => {
  require.ensure(['../components/sections/aExperience'], () => {
    resolve(require('../components/sections/aExperience'));
  });
};
const aInterests = (resolve) => {
  require.ensure(['../components/sections/aInterests'], () => {
    resolve(require('../components/sections/aInterests'));
  });
};
const aSkills = (resolve) => {
  require.ensure(['../components/sections/aSkills'], () => {
    resolve(require('../components/sections/aSkills'));
  });
};
const aProjects = (resolve) => {
  require.ensure(['../components/sections/aProjects'], () => {
    resolve(require('../components/sections/aProjects'));
  });
};
const aAuth = (resolve) => {
  require.ensure(['../components/partials/aAuth'], () => {
    resolve(require('../components/partials/aAuth'));
  });
};

export const routes = [
  {
    path: '/',
    component: aAboutMe,
  },
  {
    path: '/achievements',
    component: aAwards,
  },
  {
    path: '/education',
    component: aEducation,
  },
  {
    path: '/experience',
    component: aExperience,
  },
  {
    path: '/projects',
    component: aProjects,
  },
  {
    path: '/interests',
    component: aInterests,
  },
  {
    path: '/skills',
    component: aSkills,
  },
  {
    path: '/contact-me',
    component: aAuth,
  },
];
