// get the ninja-keys element
const ninja = document.querySelector('ninja-keys');

// add the home and posts menu items
ninja.data = [{
    id: "nav-home",
    title: "Home",
    section: "Navigation",
    handler: () => {
      window.location.href = "/";
    },
  },{id: "nav-code-39-lib",
          title: "Code&#39;Lib",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/codeLib/index.html";
          },
        },{id: "nav-projects",
          title: "Projects",
          description: "A collection of innovative projects that I have contributed to and will continue to develop, spanning robotics, mechatronics, autonomous systems, and simulation.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/projects/";
          },
        },{id: "nav-repositories",
          title: "Repositories",
          description: "A showcase of projects and repositories I&#39;ve contributed to on GitHub. Explore my work in open source, development, and collaboration.",
          section: "Navigation",
          handler: () => {
            window.location.href = "/repositories/";
          },
        },{id: "nav-cv",
          title: "CV",
          description: "",
          section: "Navigation",
          handler: () => {
            window.location.href = "/CV/";
          },
        },{id: "post-useful-math-functions",
      
        title: "Useful math functions",
      
      description: "Mathematical function utility in Python",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2025/math_functions/";
        
      },
    },{id: "post-python-matplolib-exemple",
      
        title: "Python matplolib exemple",
      
      description: "Comprehensive examples showcasing matplotlib&#39;s plotting capabilities in Python, including line plots, scatter plots, ... Includes code samples and explanations.",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2025/matplotlib_exemple/";
        
      },
    },{id: "post-orthogonal-projection",
      
        title: "Orthogonal projection",
      
      description: "Code for orthogonal projection between a point and a line",
      section: "Posts",
      handler: () => {
        
          window.location.href = "/blog/2025/ortho_proj_code/";
        
      },
    },{id: "projects-beacon-robot",
          title: 'Beacon robot',
          description: "A bio-inspired eel robot for underwater and underground exploration",
          section: "Projects",handler: () => {
              window.location.href = "/projects/1_project/";
            },},{
      id: 'light-theme',
      title: 'Change theme to light',
      description: 'Change the theme of the site to Light',
      section: 'Theme',
      handler: () => {
        setThemeSetting("light");
      },
    },
    {
      id: 'dark-theme',
      title: 'Change theme to dark',
      description: 'Change the theme of the site to Dark',
      section: 'Theme',
      handler: () => {
        setThemeSetting("dark");
      },
    },
    {
      id: 'system-theme',
      title: 'Use system default theme',
      description: 'Change the theme of the site to System Default',
      section: 'Theme',
      handler: () => {
        setThemeSetting("system");
      },
    },];
