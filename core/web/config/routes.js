export default [
  // {
  //   path: '/404',
  //   component: '404',
  // },
  {
    path: '/user',
    layout: false,
    routes: [
      {
        path: '/user/login',
        layout: false,
        name: 'login',
        component: './user/Login',
      },
      {
        path: '/user',
        redirect: '/user/login',
      },
      {
        name: 'register-result',
        icon: 'smile',
        path: '/user/register-result',
        component: './user/register-result',
      },
      {
        name: 'register',
        icon: 'smile',
        path: '/user/register',
        component: './user/register',
      },
      {
        component: '404',
      },
    ],
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    icon: 'dashboard',
    component: './dashboard/analysis',
    access: 'user',
  },
  {
    icon: 'table',
    name: 'System profiles',
    path: '/system-profiles',
    component: './system-profiles/list',
    access: 'user',
  },
  {
    name: 'Assets',
    icon: 'appstore',
    path: '/assets',
    component: './assets/list',
    access: 'user',
    // routes: [
    //   {
    //     path: '/assets',
    //     redirect: '/assets/dashboard'
    //   },
    //   {
    //     path: '/assets/dashboard',
    //     name: 'Dashboard assets',
    //     component: './assets/dashboard',
    //   },
    //   {
    //     path: '/assets/list',
    //     name: 'List assets',
    //     component: './assets/list',
    //   },
    // ],
  },
  {
    name: 'Countermeasures',
    icon: 'safety-certificate',
    path: '/countermeasures',
    component: './countermeasures/list',
    access: 'user',
    // routes: [
    //   {
    //     path: '/countermeasures',
    //     redirect: '/countermeasures/dashboard'
    //   },
    //   {
    //     path: '/countermeasures/dashboard',
    //     name: 'Dashboard countermeasures',
    //     component: './countermeasures/dashboard',
    //   },
    //   {
    //     path: '/countermeasures/list',
    //     name: 'List countermeasures',
    //     component: './countermeasures/list',
    //   },
    // ],
  },
  {
    name: 'Deployment scenarios',
    icon: 'pushpin',
    path: '/deployment-scenarios',
    component: './deployment-scenarios',
    access: 'user',
  },
  {
    name: 'Risk assessment',
    icon: 'security-scan',
    path: '/risk-assessments',
    component: './risk-assessments',
    access: 'user',
  },
  {
    name: 'Risk monitoring',
    icon: 'monitor',
    path: '/risk-monitoring',
    component: './risk-monitoring',
    access: 'user',
  },
  {
    path: '/data/cve/:id',
    component: './data/cve/$id',
  },
  {
    path: '/data/cwe/:id',
    component: './data/cwe/$id',
  },
  {
    name: 'User managerment',
    icon: 'team',
    path: '/admin/users',
    component: './admin/users',
    access: 'admin',
  },
  {
    path: '/data',
    name: 'data',
    icon: 'dashboard',
    routes: [
      {
        path: '/data',
        redirect: '/data/cwe',
      },
      {
        name: 'cve',
        icon: 'smile',
        path: '/data/cve',
        component: './data/cve',
      },
      // {
      //   name: 'cpe',
      //   icon: 'smile',
      //   path: '/data/cpe',
      //   component: './data/cpe',
      // },
      {
        name: 'cwe',
        icon: 'smile',
        path: '/data/cwe',
        component: './data/cwe',
      },
      // {
      //   name: 'Parameters',
      //   icon: 'smile',
      //   path: '/data/parameters',
      //   component: './data/parameters',
      // },
    ],
  },
  {
    path: '/system-profiles/:id',
    component: './system-profiles/$id',
    access: 'user',
  },
  {
    path: '/deployment-scenarios/mapping/:id',
    component: './deployment-scenarios/mapping/$id',
    access: 'user',
  },
  {
    path: '/deployment-scenarios/:id',
    component: './deployment-scenarios/$id',
    access: 'user',
  },
  {
    path: '/risk-assessments/assessments/:id',
    component: './risk-assessments/assessments/$id',
    access: 'user',
  },
  {
    path: '/risk-assessments/:id',
    component: './risk-assessments/$id',
    access: 'user',
  },
  {
    path: '/risk-monitoring/monitoring/:id',
    component: './risk-monitoring/monitoring/$id',
    access: 'user',
  },
  // {
  //   path: '/deployment-scenarios/assessments/:id',
  //   component: './deployment-scenarios/assessments/$id',
  // },
  {
    path: '/',
    redirect: '/dashboard',
  },
  {
    component: '404',
  },
];
