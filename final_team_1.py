<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta charset="utf-8">
  <title>
  cdr4eelz / foodie 
  / source  / final_team_1.py
 &mdash; Bitbucket
</title>
  <link rel="icon" type="image/png" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/img/favicon.png">
  <meta id="bb-canon-url" name="bb-canon-url" content="https://bitbucket.org">
  
  
<link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/compressed/css/56097c5c510e.css" type="text/css" />
<link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/compressed/css/b6644238d9ce.css" type="text/css" />

  <!--[if lt IE 9]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/css/aui/aui-ie.css" media="all"><![endif]-->
  <!--[if IE 9]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/css/aui/aui-ie9.css" media="all"><![endif]-->
  <!--[if IE]><link rel="stylesheet" href="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/css/aui-overrides-ie.css" media="all"><![endif]-->
  <meta name="description" content=""/>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="Bitbucket" />
  
  <link href="/cdr4eelz/foodie/rss?token=239fc7bbc82a12283adcca74732594a4" rel="alternate nofollow" type="application/rss+xml" title="RSS feed for foodie" />

  
<script type="text/javascript">var NREUMQ=NREUMQ||[];NREUMQ.push(["mark","firstbyte",new Date().getTime()]);</script></head>
<body class="production "
      data-base-url="https://bitbucket.org"
      data-no-avatar-image="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/img/default_avatar/16/user_blue.png"
      data-current-user="{&quot;username&quot;: &quot;fionaroni&quot;, &quot;displayName&quot;: &quot;fionaroni&quot;, &quot;firstName&quot;: &quot;&quot;, &quot;avatarUrl&quot;: &quot;https://secure.gravatar.com/avatar/97bf3821d5aa12d44697f2549fd24ddf?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F775588465b77%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&amp;s=32&quot;, &quot;lastName&quot;: &quot;&quot;, &quot;isTeam&quot;: false, &quot;isSshEnabled&quot;: false, &quot;isKbdShortcutsEnabled&quot;: true, &quot;id&quot;: 1507978, &quot;isAuthenticated&quot;: true}"
      
       data-current-repo="{&quot;scm&quot;: &quot;git&quot;, &quot;language&quot;: &quot;python&quot;, &quot;creator&quot;: {&quot;username&quot;: &quot;cdr4eelz&quot;}, &quot;id&quot;: 3439168, &quot;readOnly&quot;: false, &quot;mainbranch&quot;: {&quot;name&quot;: &quot;master&quot;}, &quot;owner&quot;: {&quot;username&quot;: &quot;cdr4eelz&quot;, &quot;isTeam&quot;: false}, &quot;pygmentsLanguage&quot;: &quot;python&quot;, &quot;slug&quot;: &quot;foodie&quot;}"
       data-current-cset="6e9f7208836615a94d00ac0a552cbd0dc9881b63"
      
      
      
      >
<script type="text/javascript" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/compressed/js/e98deabf8a2e.js"></script>

<div id="page">
  <div id="wrapper">
    
  


    <header id="header" role="banner">
      
  
    
  

      <nav class="aui-header aui-dropdown2-trigger-group" role="navigation">
        <div class="aui-header-inner">
          <div class="aui-header-primary">
            
  
    
  

            
              <h1 class="aui-header-logo aui-header-logo-bitbucket ">
                <a href="/" class="aui-nav-imagelink" id="logo-link">
                  <span class="aui-header-logo-device">Bitbucket</span>
                </a>
              </h1>
            
            
  <script id="repo-dropdown-template" type="text/html">
  

[[#hasViewed]]
  <div class="aui-dropdown2-section">
    <strong class="viewed">Recently viewed</strong>
    <ul class="aui-list-truncate">
      [[#viewed]]
        <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
          <a href="[[url]]" title="[[owner]]/[[name]]" class=" aui-icon-container">
            <img class="repo-avatar size16" src="[[{avatar}]]" alt="[[owner]]/[[name]] avatar"/>
            [[owner]] / [[name]]
          </a>
        </li>
      [[/viewed]]
    </ul>
  </div>
[[/hasViewed]]
[[#hasUpdated]]
<div class="aui-dropdown2-section">
  <strong class="updated">Recently updated</strong>
  <ul class="aui-list-truncate">
    [[#updated]]
    <li class="[[#is_private]]private[[/is_private]][[^is_private]]public[[/is_private]] repository">
      <a href="[[url]]" title="[[owner]]/[[name]]" class=" aui-icon-container">
        <img class="repo-avatar size16" src="[[{avatar}]]" alt="[[owner]]/[[name]] avatar"/>
        [[owner]] / [[name]]
      </a>
    </li>
    [[/updated]]
  </ul>
</div>
[[/hasUpdated]]

</script>
  <ul role="menu" class="aui-nav">
    
      <li>
        <a class="aui-dropdown2-trigger selected"
           aria-owns="repo-dropdown" aria-haspopup="true" href="/repo/mine " id="repositories-dropdown-trigger">
          Repositories
          <span class="aui-icon-dropdown"></span>
        </a>
        <nav id="repo-dropdown" class="aui-dropdown2 aui-style-default">
          <div id="repo-dropdown-recent"></div>
          <div class="aui-dropdown2-section">
            <ul>
              <li>
                <a href="/repo/create" class="new-repository" id="create-repo-link">
                  Create repository
                </a>
              </li>
              <li>
                <a href="/repo/import" class="import-repository" id="import-repo-link">
                  Import repository
                </a>
              </li>
            </ul>
          </div>
        </nav>
      </li>
      <li>
        <a class="aui-button aui-button-primary aui-style" href="/repo/create" id="repo-create-cta">
          Create
        </a>
      </li>
    
  </ul>

          </div>
          <div class="aui-header-secondary">
            
  <ul role="menu" class="aui-nav">
    <li>
      <form action="/repo/all" method="get" class="aui-quicksearch">
        <label for="search-query" class="assistive">owner/repository</label>
        <input id="search-query" class="search" type="text" placeholder="owner/repository" name="name">
      </form>
    </li>
    <li>
      <a class="aui-dropdown2-trigger"aria-controls="header-help-dropdown" aria-owns="header-help-dropdown"
         aria-haspopup="true" data-container="#header .aui-header-inner" href="#header-help-dropdown">
        <span class="aui-icon aui-icon-small aui-iconfont-help">Help</span><span class="aui-icon-dropdown"></span>
      </a>
      <nav id="header-help-dropdown" class="aui-dropdown2 aui-style-default aui-dropdown2-in-header" aria-hidden="true">
        <div class="aui-dropdown2-section">
          <ul>
            <li>
              <a href="/whats-new" id="features-link">
                Latest features
              </a>
            </li>
          </ul>
        </div>
        <div class="aui-dropdown2-section">
          <ul>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="DocumentationHome"
                 href="https://confluence.atlassian.com/x/bgozDQ"
                 target="_blank">
                Documentation
              </a>
            </li>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="Documentation101"
                 href="https://confluence.atlassian.com/x/cgozDQ"
                 target="_blank">
                Bitbucket 101
              </a>
            </li>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="DocumentationKB"
                 href="https://confluence.atlassian.com/x/2w4zDQ"
                 target="_blank">
                Knowledge base
              </a>
            </li>
          </ul>
        </div>
        <div class="aui-dropdown2-section">
          <ul>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="Answers"
                 href="https://answers.atlassian.com/tags/bitbucket/"
                 target="_blank">
                Bitbucket on Atlassian Answers
              </a>
            </li>
            <li>
              <a class="support-ga"
                 data-support-gaq-page="Home"
                 href="/support">
              Support
            </a>
            </li>
          </ul>
        </div>
      </nav>
    </li>
      
        
      
    
      <li>
        <a class="aui-dropdown2-trigger"
           aria-owns="user-dropdown" aria-haspopup="true" data-container="#header .aui-header-inner"
           href="/fionaroni" title="fionaroni" id="user-dropdown-trigger">
          <div class="aui-avatar aui-avatar-small">
              <div class="aui-avatar-inner">
                  <img src="https://secure.gravatar.com/avatar/97bf3821d5aa12d44697f2549fd24ddf?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F775588465b77%2Fimg%2Fdefault_avatar%2F32%2Fuser_blue.png&amp;s=32" alt="fionaroni" height="24" width="24" />
              </div>
          </div>
        </a>
        <nav id="user-dropdown" class="aui-dropdown2 aui-style-default" aria-hidden="true">
          <div class="aui-dropdown2-section">
            <ul>
              <li>
                <a href="/fionaroni" id="profile-link">View profile</a>
              </li>
              <li>
                <a href="/account/user/fionaroni/" id="account-link">Manage account</a>
              </li>
              <li>
                  <a href="/account/notifications/" id="inbox-link">Inbox <span id="inbox-unread-count"></span></a>
              </li>
              <li>
                <a href="/account/signout/">Log out</a>
              </li>
            </ul>
          </div>
            <div class="aui-dropdown2-section" id="account-admin-links">
              <strong>Teams</strong>
                <ul class="aui-list-truncate">
                </ul>
              </div>
            <div class="aui-dropdown2-section">
              <ul>
                <li>
                  <a href="#general-invite" class="general-invite-link" id="general-invite-dropdown">Invite a friend</a>
                </li>
              </ul>
              <script id="general-invite-template" type="text/html">
  
<div id="general-invite">
  <form class="aui invitation-form" id="general-invite-form" method="post" novalidate>
    <div class="error aui-message hidden">
      <span class="aui-icon icon-error"></span>
      <div class="message"></div>
    </div>
    <div class="field-group">
      <label for="id_general_email_address">Email address</label>
      <input type="email" id="id_general_email_address" name="email-address" class="text">
    </div>
    
  </form>
</div>

</script>
            </div>
            
            <div class="aui-dropdown2-section">
              <ul>
                <li>
                  <a href="/account/create-team/"
                     data-modules="registration/create-team-link"
                     id="create-team-link">Create team</a>
                </li>
                <li>
                  <a href="/account/user/fionaroni/convert-team/">Convert to team</a>
                </li>
              </ul>
            </div>
          
        </nav>
      </li>
    
  </ul>

          </div>
        </div>
      </nav>
    </header>

    
  <header id="account-warning" role="banner"
          class="aui-message-banner warning ">
    <div class="center-content">
      <span class="aui-icon aui-icon-warning"></span>
      <span class="message">
        
      </span>
    </div>
  </header>

    
    
      <header id="aui-message-bar">
        
      </header>
    


    
  <header id="repo-warning" role="banner" class="aui-message-banner warning">
    <div class="center-content">
      <span class="aui-icon aui-icon-warning"></span>
      <span class="message">
      </span>
    </div>
  </header>
  <script id="repo-warning-template" type="text/html">
  




  This repository's ownership is pending transfer to <a href="/[[username]]">[[username]]</a>.
  Visit the <a href="/cdr4eelz/foodie/admin/transfer">transfer repository page</a> to view more details.


</script>
  <header id="repo-header" class="subhead row" data-modules="repo/index">
    <div class="center-content">
      <div class="repo-summary with-repo-watch">
        <a class="repo-avatar-link" href="/cdr4eelz/foodie">
          <span class="repo-avatar-container size64" title="cdr4eelz/foodie">
  <img alt="cdr4eelz/foodie" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/img/language-avatars/python_64.png">
</span>

          
          <span class="locked" rel="tooltip" title="Private repository" data-placement="bottom"></span>
          
        </a>
        <h1><a class="repo-link" href="/cdr4eelz/foodie">foodie</a></h1>
        <ul class="repo-metadata clearfix">
          <li>
            <a class="user" href="/cdr4eelz">
              <span class="aui-icon aui-icon-small aui-iconfont-user">User icon</span>
              <span>cdr4eelz</span>
            </a>
          </li>
          
          
          
          <li class="social">
            <a class="share" href="#share" id="repo-share-link">
              <span class="aui-icon aui-icon-small aui-iconfont-email"></span>
              <span>Share</span>
            </a>
            
<div id="share" data-modules="repo/share"
     data-access-url="/cdr4eelz/foodie/admin/access"
     data-groups-url="/account/user/cdr4eelz/groups/">
  
    
          <div class="clearfix">
            <span class="repo-avatar-container size32" title="cdr4eelz/foodie">
  <img alt="cdr4eelz/foodie" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/img/language-avatars/python_32.png">
</span>

            <span class="repo-name-container">
              cdr4eelz / foodie
            </span>
          </div>
          <p class="helptext">
            
              Existing users are granted access to this repository immediately.
              New users will be sent an invitation.
            
          </p>
          <div class="share-form"></div>
    
  
  <script id="share-form-template" type="text/html">
  

<div class="error aui-message hidden">
  <span class="aui-icon icon-error"></span>
  <div class="message"></div>
</div>
<table class="widget bb-list aui">
  <thead>
  <tr class="assistive">
    <th class="user">User</th>
    <th class="role">Role</th>
    <th class="actions">Actions</th>
  </tr>
  </thead>
  <tbody>
  <tr class="form">
    <td colspan="3">
      <form>
        <input type="text" class="user-or-email text user-input"
               placeholder="Username or email address"
               [[#disabled]]disabled[[/disabled]]>
        <button type="submit" class="aui-button aui-style" disabled>Add</button>
      </form>
    </td>
  </tr>
  </tbody>
</table>

</script>
  <script id="share-detail-template" type="text/html">
  

[[#username]]
<td class="user
           [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[displayName]]">
    <a href="/[[username]]" class="user">
      <img class="avatar avatar16" src="[[avatar]]" />
      <span>[[displayName]]</span>
    </a>
  </div>
</td>
[[/username]]
[[^username]]
<td class="email
           [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]"
    [[#error]]data-error="[[error]]"[[/error]]>
  <div title="[[email]]">
    <span class="aui-icon aui-icon-small aui-iconfont-email"></span>
    [[email]]
  </div>
</td>
[[/username]]
<td class="role
           [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    [[#group]]
      [[#hasCustomGroups]]
        <select class="group">
          [[#groups]]
            <option value="[[slug]]"
                    [[#isSelected]]selected[[/isSelected]]>
              [[name]]
            </option>
          [[/groups]]
        </select>
      [[/hasCustomGroups]]
      [[^hasCustomGroups]]
      <label>
        <input type="checkbox" class="admin"
               [[#isAdmin]]checked[[/isAdmin]]>
        Administrator
      </label>
      [[/hasCustomGroups]]
    [[/group]]
    [[^group]]
      <ul>
        <li class="permission aui-lozenge aui-lozenge-complete
                   [[^read]]aui-lozenge-subtle[[/read]]"
            data-permission="read">
          read
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
                   [[^write]]aui-lozenge-subtle[[/write]]"
            data-permission="write">
          write
        </li>
        <li class="permission aui-lozenge aui-lozenge-complete
                   [[^admin]]aui-lozenge-subtle[[/admin]]"
            data-permission="admin">
          admin
        </li>
      </ul>
    [[/group]]
  </div>
</td>
<td class="actions
           [[#hasCustomGroups]]custom-groups[[/hasCustomGroups]]">
  <div>
    <a href="#" class="delete">Delete</a>
  </div>
</td>

</script>
</div>


          </li>
          
        </ul>
      </div>
      <div id="repo-toolbar" class="bb-toolbar">
        
        <div class="aui-buttons">
          <a id="repo-clone-button" class="aui-button aui-style"
            href="https://fionaroni@bitbucket.org/cdr4eelz/foodie.git">
            <span class="aui-icon aui-icon-small aui-iconfont-devtools-clone"></span>
            <span>Clone</span>
            <span class="aui-icon-dropdown"></span>
          </a>
          
            <a id="fork-button" class="aui-button aui-style"
               href="/cdr4eelz/foodie/fork">
              <span class="aui-icon aui-icon-small aui-iconfont-devtools-fork"></span>
              <span>Fork</span>
            </a>
          
        </div>
        <div class="aui-buttons">
          <a id="compare-button" class="aui-button aui-style"
             href="/cdr4eelz/foodie/compare">
            <span class="icon compare"></span>
            <span>Compare</span>
          </a>
          <a id="pull-request-button" class="aui-button aui-style"
             href="/cdr4eelz/foodie/pull-request/new">
            <span class="aui-icon aui-icon-small aui-iconfont-devtools-pull-request">Pull request icon</span>
            <span>Pull request</span>
          </a>
        </div>
        
        
          
            

<div class="aui-buttons repo-watch">
  <a class="aui-button aui-style follow following" rel="nofollow"
    href="/cdr4eelz/foodie/follow"
    
      title="Stop watching this repository"
    
    data-prefs-url="/xhr/watch-prefs/cdr4eelz/foodie"
    data-unwatch-url="/api/1.0/repositories/unwatch/cdr4eelz/foodie"
    data-url-pullrequests="/dashboard/pullrequests/watching"
    data-url-issues="/dashboard/issues/watching"
    data-repository="cdr4eelz/foodie">
    <span class="icon watch text">Watch</span>
  </a>
  <a href="#repo-preferences" class="aui-button aui-style repo-watch">
    <span class="aui-icon-dropdown"></span>
  </a>
</div>

          
          <script id="watch-preferences-template" type="text/html">
  
<div id="repo-watch-preferences" class="repo-watch-container">
  <div class="row">
    <div class="content">
      <span class="aui-icon aui-icon-large aui-iconfont-view img-icon"></span>
      [[#watching]]
        <h2>
          You are watching this repository
        </h2>
        <p>
          
          
            Updates will appear in your <a href="/dashboard/overview">newsfeed</a>.
          
        </p>
      [[/watching]]
      [[^watching]]
        <h2>
          You are not watching this repository
        </h2>
        <p>
          Start watching to receive updates.
        </p>
      [[/watching]]
      <p>
        <a class="aui-button aui-style follow following"
          data-follow-text="Stop watching" href="#">
          [[#watching]]
            Stop watching
          [[/watching]]
          [[^watching]]
            Watch this repository
          [[/watching]]
        </a>
      </p>
    </div>
  </div>
  <div class="row">
    <div class="content"
      [[^watching]] title="You must watch this repository before you can subscribe to its notifications"[[/watching]]>
      <span class="aui-icon aui-icon-large aui-iconfont-email img-icon"></span>
      <h4 class="subscribe-title">
        Subscribe to notifications about
      </h4>
      [[#showRepo]]
        <div class="checkbox">
          <input type="checkbox" id="pref-pullrequests" name="pullrequests" [[#pullrequests]]checked[[/pullrequests]]/>
          <label for="pref-pullrequests">All pull requests</label>
        </div>
      [[/showRepo]]
      [[#showIssues]]
        <div class="checkbox">
          <input type="checkbox" id="pref-issues" name="issues" [[#issues]]checked[[/issues]]/>
          <label for="pref-issues">All issues</label>
        </div>
      [[/showIssues]]
      [[#showRepo]]
        <div class="checkbox">
          <input type="checkbox" id="pref-commits" name="commits" [[#commits]]checked[[/commits]]/>
          <label for="pref-commits">All commits</label>
        </div>
      [[/showRepo]]
      [[#showWiki]]
        <div class="checkbox">
          <input type="checkbox" id="pref-wiki" name="wiki" [[#wiki]]checked[[/wiki]]/>
          <label for="pref-wiki">All wiki changes</label>
        </div>
      [[/showWiki]]
      [[#showRepo]]
        <div class="checkbox">
          <input type="checkbox" id="pref-forks" name="forks" [[#forks]]checked[[/forks]]/>
          <label for="pref-forks">All forks</label>
        </div>
      [[/showRepo]]
    </div>
  </div>
</div>

</script>
          <script id="stop-watching-template" type="text/html">
  

<div id="stop-watching-container"
  data-manage-all-url="/account/user/fionaroni/notifications/">
  <p>
    
      You may still get notifications from previously watched items in this
      repository unless you unwatch them.
    
  </p>
  <ul class="watching">
    [[#pr_count]]
      <li>
        <a href="[[urlPullrequests]]">Pull requests</a>
        <span class="aui-badge">[[pr_count]]</span>
        <a class="unwatch" href="#unwatch-pullrequests" data-kind="pullrequest">
          Unwatch
        </a>
      </li>
    [[/pr_count]]
    [[#issue_count]]
      <li>
        <a href="[[urlIssues]]">Issues</a>
        <span class="aui-badge">[[issue_count]]</span>
        <a class="unwatch" href="#unwatch-issues" data-kind="issues">
          Unwatch
        </a>
      </li>
    [[/issue_count]]
  </ul>
</div>

</script>
          <script id="preference-error-template" type="text/html">
  
<div class="aui-message error repo-watch">
  <p>An error has occurred.</p>
  <span class="aui-icon aui-icon-small aui-iconfont-error"></span>
</div>

</script>
        
        

<div id="repo-clone-dialog" class="clone-dialog hidden">
  
<div class="clone-url">
  <div class="aui-buttons">
    <a href="https://fionaroni@bitbucket.org/cdr4eelz/foodie.git"
       class="aui-button aui-style aui-dropdown2-trigger" aria-haspopup="true"
       aria-owns="clone-url-dropdown-header">
      <span class="dropdown-text">HTTPS</span>
    </a>
    <div id="clone-url-dropdown-header" class="aui-dropdown2 aui-style-default">
      <ul class="aui-list-truncate">
        <li>
          <a href="https://fionaroni@bitbucket.org/cdr4eelz/foodie.git"
            
              data-command="git clone https://fionaroni@bitbucket.org/cdr4eelz/foodie.git"
            
            class="item-link https">HTTPS
          </a>
        </li>
        <li>
          <a href="ssh://git@bitbucket.org/cdr4eelz/foodie.git"
            
              data-command="git clone git@bitbucket.org:cdr4eelz/foodie.git"
            
            class="item-link ssh">SSH
          </a>
        </li>
      </ul>
    </div>
    <input type="text" readonly="readonly" value="git clone https://fionaroni@bitbucket.org/cdr4eelz/foodie.git">
  </div>
  
  <p>Need help cloning? Visit
     <a href="https://confluence.atlassian.com/x/cgozDQ" target="_blank">Bitbucket 101</a>.</p>
  
</div>


  
  
  

<div class="clone-in-sourcetree"
  data-https-url="https://fionaroni@bitbucket.org/cdr4eelz/foodie.git"
  data-ssh-url="ssh://git@bitbucket.org/cdr4eelz/foodie.git">
  <p><button class="aui-button aui-style aui-button-primary">Clone in SourceTree</button></p>


  <p class="windows-text">
      
        <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_win" target="_blank">SourceTree</a>
        is a free Windows client by Atlassian for Git, Mercurial, and Subversion.
      
  </p>
  <p class="mac-text">
      
        <a href="http://www.sourcetreeapp.com/?utm_source=internal&amp;utm_medium=link&amp;utm_campaign=clone_repo_mac" target="_blank">SourceTree</a>
        is a free Mac client by Atlassian for Git, Mercurial, and Subversion.
      
  </p>
</div>

  
</div>

      </div>
    </div>
    <div class="clearfix"></div>
  </header>
  <nav id="repo-tabs" class="aui-navgroup aui-navgroup-horizontal aui-navgroup-horizontal-roomy">
    <div class="aui-navgroup-inner">
      <div class="aui-navgroup-primary">
        <ul class="aui-nav">
          
            <li>
              <a href="/cdr4eelz/foodie/overview" id="repo-overview-link">Overview</a>
            </li>
          
          
            <li class="aui-nav-selected">
              <a href="/cdr4eelz/foodie/src" id="repo-source-link">Source</a>
            </li>
          
          
            <li>
              <a href="/cdr4eelz/foodie/commits" id="repo-commits-link">
                Commits
              </a>
            </li>
          
          
            <li>
              <a href="/cdr4eelz/foodie/pull-requests" id="repo-pullrequests-link">
                Pull requests
                
                  
                
              </a>
            </li>
          
          
            
          
            <li id="issues-tab" class="
              
                hidden
              
            ">
              <a href="/cdr4eelz/foodie/issues?status=new&amp;status=open" id="repo-issues-link">
                Issues
                
                  
                
              </a>
            </li>
            <li id="wiki-tab" class="
                
                  hidden
                
              ">
              <a href="/cdr4eelz/foodie/wiki" id="repo-wiki-link">Wiki</a>
            </li>
          
            <li>
            <a href="/cdr4eelz/foodie/downloads" id="repo-downloads-link">
              Downloads
              
                
              
            </a>
            </li>
          
        </ul>
      </div>
      <div class="aui-navgroup-secondary">
        <ul class="aui-nav">
          
            <li id="admin-tab">
              <a href="/cdr4eelz/foodie/admin"
                  id="repo-admin-link" title="Administration">
                  <span class="aui-icon aui-icon-small aui-iconfont-configure">Administration</span>
              </a>
            </li>
          
        </ul>
      </div>
    </div>
  </nav>


    <div id="content" role="main">
      
  <div id="repo-content">
    
  <div id="source-container" data-modules="repo/source/index">
    



<header id="source-path">
  
  <div class="labels labels-csv">
    
      <div class="aui-buttons">
        <button data-branches-tags-url="/api/1.0/repositories/cdr4eelz/foodie/branches-tags"
                data-modules="components/branch-dialog"
                class="aui-button aui-style branch-dialog-trigger" title="master">
          
            
              <span class="aui-icon aui-icon-small aui-iconfont-devtools-branch">Branch</span>
            
            <span class="name">master</span>
          
          <span class="aui-icon-dropdown"></span>
        </button>
      </div>
    
  </div>
  
  
    <div class="view-switcher">
      <div class="aui-buttons">
        
          <a href="/cdr4eelz/foodie/src/6e9f72088366/final_team_1.py?at=master"
             class="aui-button aui-style pjax-trigger" aria-pressed="true">
            Source
          </a>
          <a href="/cdr4eelz/foodie/diff/final_team_1.py?diff2=6e9f72088366&at=master"
             class="aui-button aui-style pjax-trigger"
             title="Diff to previous change">
            Diff
          </a>
          <a href="/cdr4eelz/foodie/history-node/6e9f72088366/final_team_1.py?at=master"
             class="aui-button aui-style pjax-trigger">
            History
          </a>
        
      </div>
    </div>
  
  <h1>
    <a href="/cdr4eelz/foodie/src/6e9f72088366?at=master"
       class="pjax-trigger" title="cdr4eelz/foodie at 6e9f72088366">foodie</a> /
    
      
        
          <span>final_team_1.py</span>
        
      
    
  </h1>
  
    
    
  
  <div class="clearfix"></div>
</header>


  
    <div id="editor-container" class="maskable"
         data-owner="cdr4eelz"
         data-slug="foodie"
         data-is-writer="true"
         data-has-push-access="true"
         data-hash="6e9f7208836615a94d00ac0a552cbd0dc9881b63"
         data-branch="master"
         data-path="final_team_1.py"
         data-source-url="/api/1.0/repositories/cdr4eelz/foodie/src/6e9f7208836615a94d00ac0a552cbd0dc9881b63/final_team_1.py">
      <div id="source-view" data-modules="repo/source/view-file">
        <div class="toolbar">
          <div class="primary">
            <div class="aui-buttons">
              
                <button id="file-history-trigger" class="aui-button aui-style changeset-info"
                        data-changeset="a5487a0b00f2864c4fd52ef0c9bd8c8030e91588"
                        data-path="final_team_1.py"
                        data-current="6e9f7208836615a94d00ac0a552cbd0dc9881b63">
                  
                     

<img class="avatar avatar16" src="https://secure.gravatar.com/avatar/43296b70eb96643c8b57f5e652940f82?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F775588465b77%2Fimg%2Fdefault_avatar%2F16%2Fuser_blue.png&amp;s=16" alt="Erik Rogers avatar" />
<span class="changeset-hash">6e9f720</span>
<time datetime="2013-08-16T17:31:58+00:00" class="timestamp"></time>
<span class="aui-icon-dropdown"></span>

                  
                </button>
              
            </div>
          <a href="/cdr4eelz/foodie/full-commit/6e9f72088366/final_team_1.py" id="full-commit-link"
              title="View full commit 6e9f720">Full commit</a>
          </div>
            <div class="secondary">
              <div class="aui-buttons">
                
                  <a href="/cdr4eelz/foodie/annotate/6e9f7208836615a94d00ac0a552cbd0dc9881b63/final_team_1.py?at=master"
                  class="aui-button aui-style pjax-trigger">Blame</a>
                
                
                <a href="/cdr4eelz/foodie/raw/6e9f7208836615a94d00ac0a552cbd0dc9881b63/final_team_1.py"
                  class="aui-button aui-style">Raw</a>
              </div>
              
                
                  <div class="aui-buttons">
                    
                      <span class="edit-button-overlay" title="You can only edit the latest revision of a branch."></span>
                    
                    <button class="edit-button aui-button aui-style" disabled="disabled" aria-disabled="true">Edit</button>
                  </div>
                
              
            </div>
          <div class="clearfix"></div>
        </div>

        
          
            
              
                <div class="file-source">
                  <table class="highlighttable"><tr><td class="linenos"><div class="linenodiv"><pre><a href="#cl-1">  1</a>
<a href="#cl-2">  2</a>
<a href="#cl-3">  3</a>
<a href="#cl-4">  4</a>
<a href="#cl-5">  5</a>
<a href="#cl-6">  6</a>
<a href="#cl-7">  7</a>
<a href="#cl-8">  8</a>
<a href="#cl-9">  9</a>
<a href="#cl-10"> 10</a>
<a href="#cl-11"> 11</a>
<a href="#cl-12"> 12</a>
<a href="#cl-13"> 13</a>
<a href="#cl-14"> 14</a>
<a href="#cl-15"> 15</a>
<a href="#cl-16"> 16</a>
<a href="#cl-17"> 17</a>
<a href="#cl-18"> 18</a>
<a href="#cl-19"> 19</a>
<a href="#cl-20"> 20</a>
<a href="#cl-21"> 21</a>
<a href="#cl-22"> 22</a>
<a href="#cl-23"> 23</a>
<a href="#cl-24"> 24</a>
<a href="#cl-25"> 25</a>
<a href="#cl-26"> 26</a>
<a href="#cl-27"> 27</a>
<a href="#cl-28"> 28</a>
<a href="#cl-29"> 29</a>
<a href="#cl-30"> 30</a>
<a href="#cl-31"> 31</a>
<a href="#cl-32"> 32</a>
<a href="#cl-33"> 33</a>
<a href="#cl-34"> 34</a>
<a href="#cl-35"> 35</a>
<a href="#cl-36"> 36</a>
<a href="#cl-37"> 37</a>
<a href="#cl-38"> 38</a>
<a href="#cl-39"> 39</a>
<a href="#cl-40"> 40</a>
<a href="#cl-41"> 41</a>
<a href="#cl-42"> 42</a>
<a href="#cl-43"> 43</a>
<a href="#cl-44"> 44</a>
<a href="#cl-45"> 45</a>
<a href="#cl-46"> 46</a>
<a href="#cl-47"> 47</a>
<a href="#cl-48"> 48</a>
<a href="#cl-49"> 49</a>
<a href="#cl-50"> 50</a>
<a href="#cl-51"> 51</a>
<a href="#cl-52"> 52</a>
<a href="#cl-53"> 53</a>
<a href="#cl-54"> 54</a>
<a href="#cl-55"> 55</a>
<a href="#cl-56"> 56</a>
<a href="#cl-57"> 57</a>
<a href="#cl-58"> 58</a>
<a href="#cl-59"> 59</a>
<a href="#cl-60"> 60</a>
<a href="#cl-61"> 61</a>
<a href="#cl-62"> 62</a>
<a href="#cl-63"> 63</a>
<a href="#cl-64"> 64</a>
<a href="#cl-65"> 65</a>
<a href="#cl-66"> 66</a>
<a href="#cl-67"> 67</a>
<a href="#cl-68"> 68</a>
<a href="#cl-69"> 69</a>
<a href="#cl-70"> 70</a>
<a href="#cl-71"> 71</a>
<a href="#cl-72"> 72</a>
<a href="#cl-73"> 73</a>
<a href="#cl-74"> 74</a>
<a href="#cl-75"> 75</a>
<a href="#cl-76"> 76</a>
<a href="#cl-77"> 77</a>
<a href="#cl-78"> 78</a>
<a href="#cl-79"> 79</a>
<a href="#cl-80"> 80</a>
<a href="#cl-81"> 81</a>
<a href="#cl-82"> 82</a>
<a href="#cl-83"> 83</a>
<a href="#cl-84"> 84</a>
<a href="#cl-85"> 85</a>
<a href="#cl-86"> 86</a>
<a href="#cl-87"> 87</a>
<a href="#cl-88"> 88</a>
<a href="#cl-89"> 89</a>
<a href="#cl-90"> 90</a>
<a href="#cl-91"> 91</a>
<a href="#cl-92"> 92</a>
<a href="#cl-93"> 93</a>
<a href="#cl-94"> 94</a>
<a href="#cl-95"> 95</a>
<a href="#cl-96"> 96</a>
<a href="#cl-97"> 97</a>
<a href="#cl-98"> 98</a>
<a href="#cl-99"> 99</a>
<a href="#cl-100">100</a>
<a href="#cl-101">101</a>
<a href="#cl-102">102</a>
<a href="#cl-103">103</a>
<a href="#cl-104">104</a>
<a href="#cl-105">105</a>
<a href="#cl-106">106</a>
<a href="#cl-107">107</a>
<a href="#cl-108">108</a>
<a href="#cl-109">109</a>
<a href="#cl-110">110</a>
<a href="#cl-111">111</a>
<a href="#cl-112">112</a>
<a href="#cl-113">113</a>
<a href="#cl-114">114</a>
<a href="#cl-115">115</a>
<a href="#cl-116">116</a>
<a href="#cl-117">117</a>
<a href="#cl-118">118</a>
<a href="#cl-119">119</a>
<a href="#cl-120">120</a>
<a href="#cl-121">121</a>
<a href="#cl-122">122</a>
<a href="#cl-123">123</a>
<a href="#cl-124">124</a>
<a href="#cl-125">125</a>
<a href="#cl-126">126</a>
<a href="#cl-127">127</a>
<a href="#cl-128">128</a>
<a href="#cl-129">129</a>
<a href="#cl-130">130</a>
<a href="#cl-131">131</a>
<a href="#cl-132">132</a>
<a href="#cl-133">133</a>
<a href="#cl-134">134</a>
<a href="#cl-135">135</a>
<a href="#cl-136">136</a>
<a href="#cl-137">137</a>
<a href="#cl-138">138</a>
<a href="#cl-139">139</a>
<a href="#cl-140">140</a>
<a href="#cl-141">141</a>
<a href="#cl-142">142</a>
<a href="#cl-143">143</a>
<a href="#cl-144">144</a>
<a href="#cl-145">145</a>
<a href="#cl-146">146</a>
<a href="#cl-147">147</a>
<a href="#cl-148">148</a>
<a href="#cl-149">149</a>
<a href="#cl-150">150</a>
<a href="#cl-151">151</a>
<a href="#cl-152">152</a>
<a href="#cl-153">153</a>
<a href="#cl-154">154</a>
<a href="#cl-155">155</a>
<a href="#cl-156">156</a>
<a href="#cl-157">157</a>
<a href="#cl-158">158</a>
<a href="#cl-159">159</a>
<a href="#cl-160">160</a>
<a href="#cl-161">161</a>
<a href="#cl-162">162</a>
<a href="#cl-163">163</a>
<a href="#cl-164">164</a>
<a href="#cl-165">165</a>
<a href="#cl-166">166</a>
<a href="#cl-167">167</a>
<a href="#cl-168">168</a>
<a href="#cl-169">169</a>
<a href="#cl-170">170</a>
<a href="#cl-171">171</a>
<a href="#cl-172">172</a>
<a href="#cl-173">173</a>
<a href="#cl-174">174</a>
<a href="#cl-175">175</a>
<a href="#cl-176">176</a>
<a href="#cl-177">177</a>
<a href="#cl-178">178</a>
<a href="#cl-179">179</a>
<a href="#cl-180">180</a>
<a href="#cl-181">181</a>
<a href="#cl-182">182</a>
<a href="#cl-183">183</a>
<a href="#cl-184">184</a>
<a href="#cl-185">185</a>
<a href="#cl-186">186</a>
<a href="#cl-187">187</a>
<a href="#cl-188">188</a>
<a href="#cl-189">189</a>
<a href="#cl-190">190</a>
<a href="#cl-191">191</a>
<a href="#cl-192">192</a>
<a href="#cl-193">193</a>
<a href="#cl-194">194</a>
<a href="#cl-195">195</a>
<a href="#cl-196">196</a>
<a href="#cl-197">197</a>
<a href="#cl-198">198</a>
<a href="#cl-199">199</a>
<a href="#cl-200">200</a>
<a href="#cl-201">201</a>
<a href="#cl-202">202</a>
<a href="#cl-203">203</a>
<a href="#cl-204">204</a>
<a href="#cl-205">205</a>
<a href="#cl-206">206</a>
<a href="#cl-207">207</a>
<a href="#cl-208">208</a>
<a href="#cl-209">209</a>
<a href="#cl-210">210</a>
<a href="#cl-211">211</a>
<a href="#cl-212">212</a>
<a href="#cl-213">213</a>
<a href="#cl-214">214</a>
<a href="#cl-215">215</a>
<a href="#cl-216">216</a>
<a href="#cl-217">217</a>
<a href="#cl-218">218</a>
<a href="#cl-219">219</a>
<a href="#cl-220">220</a>
<a href="#cl-221">221</a>
<a href="#cl-222">222</a>
<a href="#cl-223">223</a>
<a href="#cl-224">224</a>
<a href="#cl-225">225</a>
<a href="#cl-226">226</a>
<a href="#cl-227">227</a>
<a href="#cl-228">228</a>
<a href="#cl-229">229</a>
<a href="#cl-230">230</a>
<a href="#cl-231">231</a>
<a href="#cl-232">232</a>
<a href="#cl-233">233</a>
<a href="#cl-234">234</a>
<a href="#cl-235">235</a>
<a href="#cl-236">236</a>
<a href="#cl-237">237</a>
<a href="#cl-238">238</a>
<a href="#cl-239">239</a>
<a href="#cl-240">240</a>
<a href="#cl-241">241</a>
<a href="#cl-242">242</a>
<a href="#cl-243">243</a>
<a href="#cl-244">244</a>
<a href="#cl-245">245</a>
<a href="#cl-246">246</a>
<a href="#cl-247">247</a>
<a href="#cl-248">248</a>
<a href="#cl-249">249</a>
<a href="#cl-250">250</a>
<a href="#cl-251">251</a>
<a href="#cl-252">252</a>
<a href="#cl-253">253</a>
<a href="#cl-254">254</a>
<a href="#cl-255">255</a>
<a href="#cl-256">256</a>
<a href="#cl-257">257</a>
<a href="#cl-258">258</a>
<a href="#cl-259">259</a>
<a href="#cl-260">260</a>
<a href="#cl-261">261</a>
<a href="#cl-262">262</a>
<a href="#cl-263">263</a>
<a href="#cl-264">264</a>
<a href="#cl-265">265</a>
<a href="#cl-266">266</a>
<a href="#cl-267">267</a>
<a href="#cl-268">268</a>
<a href="#cl-269">269</a>
<a href="#cl-270">270</a>
<a href="#cl-271">271</a>
<a href="#cl-272">272</a>
<a href="#cl-273">273</a>
<a href="#cl-274">274</a>
<a href="#cl-275">275</a>
<a href="#cl-276">276</a>
<a href="#cl-277">277</a>
<a href="#cl-278">278</a>
<a href="#cl-279">279</a>
<a href="#cl-280">280</a>
<a href="#cl-281">281</a>
<a href="#cl-282">282</a>
<a href="#cl-283">283</a>
<a href="#cl-284">284</a>
<a href="#cl-285">285</a>
<a href="#cl-286">286</a>
<a href="#cl-287">287</a>
<a href="#cl-288">288</a>
<a href="#cl-289">289</a>
<a href="#cl-290">290</a>
<a href="#cl-291">291</a>
<a href="#cl-292">292</a>
<a href="#cl-293">293</a>
<a href="#cl-294">294</a>
<a href="#cl-295">295</a>
<a href="#cl-296">296</a>
<a href="#cl-297">297</a>
<a href="#cl-298">298</a>
<a href="#cl-299">299</a>
<a href="#cl-300">300</a>
<a href="#cl-301">301</a>
<a href="#cl-302">302</a>
<a href="#cl-303">303</a>
<a href="#cl-304">304</a>
<a href="#cl-305">305</a>
<a href="#cl-306">306</a>
<a href="#cl-307">307</a>
<a href="#cl-308">308</a>
<a href="#cl-309">309</a>
<a href="#cl-310">310</a>
<a href="#cl-311">311</a>
<a href="#cl-312">312</a>
<a href="#cl-313">313</a>
<a href="#cl-314">314</a>
<a href="#cl-315">315</a>
<a href="#cl-316">316</a>
<a href="#cl-317">317</a>
<a href="#cl-318">318</a>
<a href="#cl-319">319</a>
<a href="#cl-320">320</a>
<a href="#cl-321">321</a>
<a href="#cl-322">322</a>
<a href="#cl-323">323</a>
<a href="#cl-324">324</a>
<a href="#cl-325">325</a>
<a href="#cl-326">326</a>
<a href="#cl-327">327</a>
<a href="#cl-328">328</a>
<a href="#cl-329">329</a>
<a href="#cl-330">330</a>
<a href="#cl-331">331</a>
<a href="#cl-332">332</a>
<a href="#cl-333">333</a>
<a href="#cl-334">334</a>
<a href="#cl-335">335</a>
<a href="#cl-336">336</a>
<a href="#cl-337">337</a>
<a href="#cl-338">338</a>
<a href="#cl-339">339</a>
<a href="#cl-340">340</a>
<a href="#cl-341">341</a>
<a href="#cl-342">342</a>
<a href="#cl-343">343</a>
<a href="#cl-344">344</a>
<a href="#cl-345">345</a>
<a href="#cl-346">346</a>
<a href="#cl-347">347</a>
<a href="#cl-348">348</a>
<a href="#cl-349">349</a>
<a href="#cl-350">350</a>
<a href="#cl-351">351</a>
<a href="#cl-352">352</a>
<a href="#cl-353">353</a>
<a href="#cl-354">354</a>
<a href="#cl-355">355</a>
<a href="#cl-356">356</a>
<a href="#cl-357">357</a>
<a href="#cl-358">358</a>
<a href="#cl-359">359</a>
<a href="#cl-360">360</a>
<a href="#cl-361">361</a>
<a href="#cl-362">362</a>
<a href="#cl-363">363</a>
<a href="#cl-364">364</a>
<a href="#cl-365">365</a>
<a href="#cl-366">366</a>
<a href="#cl-367">367</a>
<a href="#cl-368">368</a>
<a href="#cl-369">369</a>
<a href="#cl-370">370</a>
<a href="#cl-371">371</a>
<a href="#cl-372">372</a>
<a href="#cl-373">373</a>
<a href="#cl-374">374</a>
<a href="#cl-375">375</a>
<a href="#cl-376">376</a>
<a href="#cl-377">377</a>
<a href="#cl-378">378</a>
<a href="#cl-379">379</a>
<a href="#cl-380">380</a>
<a href="#cl-381">381</a>
<a href="#cl-382">382</a>
<a href="#cl-383">383</a>
<a href="#cl-384">384</a>
<a href="#cl-385">385</a>
<a href="#cl-386">386</a>
<a href="#cl-387">387</a>
<a href="#cl-388">388</a>
<a href="#cl-389">389</a>
<a href="#cl-390">390</a>
<a href="#cl-391">391</a>
<a href="#cl-392">392</a>
<a href="#cl-393">393</a>
<a href="#cl-394">394</a>
<a href="#cl-395">395</a>
<a href="#cl-396">396</a>
<a href="#cl-397">397</a>
<a href="#cl-398">398</a>
<a href="#cl-399">399</a>
<a href="#cl-400">400</a>
<a href="#cl-401">401</a>
<a href="#cl-402">402</a>
<a href="#cl-403">403</a>
<a href="#cl-404">404</a>
<a href="#cl-405">405</a>
<a href="#cl-406">406</a>
<a href="#cl-407">407</a>
<a href="#cl-408">408</a>
<a href="#cl-409">409</a>
<a href="#cl-410">410</a>
<a href="#cl-411">411</a>
<a href="#cl-412">412</a>
<a href="#cl-413">413</a>
<a href="#cl-414">414</a>
<a href="#cl-415">415</a>
<a href="#cl-416">416</a>
<a href="#cl-417">417</a>
<a href="#cl-418">418</a>
<a href="#cl-419">419</a>
<a href="#cl-420">420</a>
<a href="#cl-421">421</a>
<a href="#cl-422">422</a>
<a href="#cl-423">423</a>
<a href="#cl-424">424</a>
<a href="#cl-425">425</a>
<a href="#cl-426">426</a>
<a href="#cl-427">427</a>
<a href="#cl-428">428</a>
<a href="#cl-429">429</a>
<a href="#cl-430">430</a>
<a href="#cl-431">431</a>
<a href="#cl-432">432</a>
<a href="#cl-433">433</a>
<a href="#cl-434">434</a>
<a href="#cl-435">435</a>
<a href="#cl-436">436</a>
<a href="#cl-437">437</a>
<a href="#cl-438">438</a>
<a href="#cl-439">439</a>
<a href="#cl-440">440</a>
<a href="#cl-441">441</a>
<a href="#cl-442">442</a>
<a href="#cl-443">443</a>
<a href="#cl-444">444</a>
<a href="#cl-445">445</a>
<a href="#cl-446">446</a>
<a href="#cl-447">447</a>
<a href="#cl-448">448</a>
<a href="#cl-449">449</a>
<a href="#cl-450">450</a>
<a href="#cl-451">451</a>
<a href="#cl-452">452</a>
<a href="#cl-453">453</a>
<a href="#cl-454">454</a>
<a href="#cl-455">455</a></pre></div></td><td class="code"><div class="highlight"><pre><a name="cl-1"></a><span class="kn">from</span> <span class="nn">random</span> <span class="kn">import</span> <span class="n">random</span> <span class="c">#import random function from the random module</span>
<a name="cl-2"></a><span class="kn">from</span> <span class="nn">random</span> <span class="kn">import</span> <span class="n">randrange</span> <span class="c">#import randrange function from the random module</span>
<a name="cl-3"></a><span class="kn">from</span> <span class="nn">collections</span> <span class="kn">import</span> <span class="n">Counter</span><span class="p">,</span><span class="n">OrderedDict</span><span class="p">,</span><span class="n">deque</span> <span class="c">#import a few classes from collections module</span>
<a name="cl-4"></a><span class="kn">from</span> <span class="nn">itertools</span> <span class="kn">import</span> <span class="n">repeat</span>
<a name="cl-5"></a><span class="kn">from</span> <span class="nn">operator</span> <span class="kn">import</span> <span class="n">itemgetter</span>
<a name="cl-6"></a>
<a name="cl-7"></a><span class="kn">import</span> <span class="nn">i155_visual</span>
<a name="cl-8"></a>
<a name="cl-9"></a><span class="k">class</span> <span class="nc">Graph</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span> <span class="c">#represents entire population of users</span>
<a name="cl-10"></a>    
<a name="cl-11"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">population</span><span class="p">):</span>
<a name="cl-12"></a>        <span class="sd">&quot;&quot;&quot;create a new graph with population users and no connections.</span>
<a name="cl-13"></a><span class="sd">        no users in the new graph should have any technology&quot;&quot;&quot;</span>
<a name="cl-14"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="o">=</span><span class="nb">dict</span><span class="p">()</span>
<a name="cl-15"></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">population</span><span class="p">):</span> <span class="c">#Go 0 to population-1</span>
<a name="cl-16"></a>            <span class="n">u</span> <span class="o">=</span> <span class="n">User</span><span class="p">(</span><span class="n">i</span><span class="p">)</span> <span class="c">#Make fresh &quot;User&quot; object with desired ID</span>
<a name="cl-17"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="p">[</span><span class="n">i</span><span class="p">]</span> <span class="o">=</span> <span class="n">u</span> <span class="c">#Map from ID(int)-&gt;User(object) in dictionary</span>
<a name="cl-18"></a>
<a name="cl-19"></a>    <span class="k">def</span> <span class="nf">circle_connect</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">n</span><span class="p">):</span>
<a name="cl-20"></a>        <span class="sd">&quot;&quot;&quot;connect each user i to the next n users, that is</span>
<a name="cl-21"></a><span class="sd">        users (i+1)%population, (i+2)%population,...,</span>
<a name="cl-22"></a><span class="sd">        (i+n)%population.&quot;&quot;&quot;</span>
<a name="cl-23"></a>        <span class="n">population</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="p">)</span>
<a name="cl-24"></a>        <span class="k">for</span> <span class="n">u</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="o">.</span><span class="n">values</span><span class="p">():</span>
<a name="cl-25"></a>            <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">n</span><span class="o">+</span><span class="mi">1</span><span class="p">):</span> <span class="c">#1 thru n</span>
<a name="cl-26"></a>                <span class="n">buddy_id</span> <span class="o">=</span> <span class="p">(</span><span class="n">u</span><span class="o">.</span><span class="n">get_id</span><span class="p">()</span><span class="o">+</span><span class="n">b</span><span class="p">)</span> <span class="o">%</span> <span class="n">population</span>
<a name="cl-27"></a>                <span class="n">buddy</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_id_to_user</span><span class="p">(</span><span class="n">buddy_id</span><span class="p">)</span>
<a name="cl-28"></a>                <span class="n">u</span><span class="o">.</span><span class="n">make_friends</span><span class="p">(</span><span class="n">buddy</span><span class="p">)</span>
<a name="cl-29"></a>
<a name="cl-30"></a>    <span class="k">def</span> <span class="nf">convert_id_to_user</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ID</span><span class="p">):</span>
<a name="cl-31"></a>        <span class="sd">&quot;&quot;&quot;Lookup a User object within our &quot;population&quot; by it&#39;s ID&quot;&quot;&quot;</span>
<a name="cl-32"></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="p">[</span><span class="n">ID</span><span class="p">]</span>
<a name="cl-33"></a>    
<a name="cl-34"></a>    <span class="k">def</span> <span class="nf">random_connections</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">num_connections</span><span class="p">):</span> 
<a name="cl-35"></a>        <span class="sd">&quot;&quot;&quot;add num_connections new connections randomly to the graph&quot;&quot;&quot;</span> 
<a name="cl-36"></a>        <span class="n">population</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="p">)</span>
<a name="cl-37"></a>        <span class="n">num</span> <span class="o">=</span> <span class="n">num_connections</span>
<a name="cl-38"></a><span class="c">#       print(&quot;Number of random connections that will be added to graph:&quot;, num)</span>
<a name="cl-39"></a>        <span class="k">while</span> <span class="n">num</span><span class="o">&gt;</span><span class="mi">0</span><span class="p">:</span>
<a name="cl-40"></a>            <span class="n">buddy1</span> <span class="o">=</span> <span class="n">randrange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">population</span><span class="p">)</span>
<a name="cl-41"></a>            <span class="n">buddy2</span> <span class="o">=</span> <span class="n">buddy1</span>
<a name="cl-42"></a>            <span class="k">while</span> <span class="n">buddy1</span> <span class="o">==</span> <span class="n">buddy2</span><span class="p">:</span>
<a name="cl-43"></a>                <span class="n">buddy2</span> <span class="o">=</span> <span class="n">randrange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span><span class="n">population</span><span class="p">)</span>
<a name="cl-44"></a><span class="c">#           print(&quot;buddy1:&quot;,buddy1) </span>
<a name="cl-45"></a><span class="c">#           print(&quot;buddy2:&quot;,buddy2)</span>
<a name="cl-46"></a>            <span class="n">buddy1</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_id_to_user</span><span class="p">(</span><span class="n">buddy1</span><span class="p">)</span>
<a name="cl-47"></a>            <span class="n">buddy2</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">convert_id_to_user</span><span class="p">(</span><span class="n">buddy2</span><span class="p">)</span>
<a name="cl-48"></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">buddy1</span><span class="o">.</span><span class="n">is_friend</span><span class="p">(</span><span class="n">buddy2</span><span class="p">):</span>
<a name="cl-49"></a>                <span class="n">buddy1</span><span class="o">.</span><span class="n">make_friends</span><span class="p">(</span><span class="n">buddy2</span><span class="p">)</span>
<a name="cl-50"></a>                <span class="n">num</span> <span class="o">-=</span> <span class="mi">1</span>
<a name="cl-51"></a>
<a name="cl-52"></a>    <span class="k">def</span> <span class="nf">is_connected</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-53"></a>        <span class="sd">&quot;&quot;&quot;returns True if there is a path from every graph User to</span>
<a name="cl-54"></a><span class="sd">        every other user&quot;&quot;&quot;</span>
<a name="cl-55"></a>        <span class="k">return</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">friends_of</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">convert_id_to_user</span><span class="p">(</span><span class="mi">0</span><span class="p">)))</span> <span class="o">==</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_users</span><span class="p">())</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-56"></a>        
<a name="cl-57"></a>    <span class="k">def</span> <span class="nf">friends_of</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">u</span><span class="p">,</span> <span class="n">ubase</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">friends</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span> <span class="c">#returns list of Users connected (by any num of degrees of separation) to User u </span>
<a name="cl-58"></a>        <span class="k">if</span> <span class="n">ubase</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-59"></a>            <span class="n">ubase</span> <span class="o">=</span> <span class="n">u</span>
<a name="cl-60"></a>        <span class="k">if</span> <span class="n">friends</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-61"></a>            <span class="n">friends</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-62"></a><span class="c">#        print(&quot;ubase=&quot;, ubase, &quot;u=&quot;, u)</span>
<a name="cl-63"></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">u</span><span class="o">.</span><span class="n">get_friends</span><span class="p">():</span><span class="c">#i = immediate friends</span>
<a name="cl-64"></a>            <span class="k">if</span> <span class="p">(</span><span class="n">i</span><span class="o">.</span><span class="n">get_id</span><span class="p">()</span> <span class="o">==</span> <span class="n">ubase</span><span class="o">.</span><span class="n">get_id</span><span class="p">()):</span>
<a name="cl-65"></a><span class="c">#                print(&#39;  base :&#39;, i)</span>
<a name="cl-66"></a>                <span class="k">pass</span>
<a name="cl-67"></a>            <span class="k">elif</span> <span class="p">(</span><span class="n">i</span> <span class="ow">in</span> <span class="n">friends</span><span class="p">):</span>
<a name="cl-68"></a><span class="c">#                print(&#39;  pass :&#39;, i)</span>
<a name="cl-69"></a>                <span class="k">pass</span>
<a name="cl-70"></a>            <span class="k">else</span><span class="p">:</span>
<a name="cl-71"></a><span class="c">#                print(&#39;  append:&#39;, i)</span>
<a name="cl-72"></a>                <span class="n">friends</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="p">)</span>
<a name="cl-73"></a><span class="c">#                print(&#39;  recur:&#39;, i, friends)</span>
<a name="cl-74"></a>                <span class="n">new_friends</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">friends_of</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">ubase</span><span class="p">,</span> <span class="n">friends</span><span class="p">)</span>
<a name="cl-75"></a>        <span class="k">return</span> <span class="n">friends</span>
<a name="cl-76"></a>
<a name="cl-77"></a>    <span class="k">def</span> <span class="nf">time_step</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-78"></a>        <span class="sd">&quot;&quot;&quot;move the simulation forward by one time period.</span>
<a name="cl-79"></a><span class="sd">        Each user adopts the most popular technology among</span>
<a name="cl-80"></a><span class="sd">        themselves and their friends.  If there are multiple</span>
<a name="cl-81"></a><span class="sd">        technologies that are tied for most popular, the user</span>
<a name="cl-82"></a><span class="sd">        selects one at random.&quot;&quot;&quot;</span>
<a name="cl-83"></a>        <span class="c"># To find the most common tech in a subset of users,</span>
<a name="cl-84"></a>        <span class="c"># you cannot build a frequency table using a</span>
<a name="cl-85"></a>        <span class="c"># dictionary since Technologies are mutable objects.</span>
<a name="cl-86"></a>        <span class="c"># If you want to follow a similar strategy, you can</span>
<a name="cl-87"></a>        <span class="c"># import the collections package and use a Counter</span>
<a name="cl-88"></a>        <span class="c"># object, which works like a (slow) dictionary for</span>
<a name="cl-89"></a>        <span class="c"># mutable objects.  However, there are many other</span>
<a name="cl-90"></a>        <span class="c"># strategies that you could use to do the same thing.</span>
<a name="cl-91"></a>        
<a name="cl-92"></a>        <span class="n">next_tech</span> <span class="o">=</span> <span class="nb">dict</span><span class="p">()</span> <span class="c">#A temporary dictionary using User&#39;s ID (int)</span>
<a name="cl-93"></a>        <span class="c">#FIRST we must make each user decide on a technology</span>
<a name="cl-94"></a>        <span class="k">for</span> <span class="n">user</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="o">.</span><span class="n">values</span><span class="p">():</span> <span class="c">#Iterating over User objects</span>
<a name="cl-95"></a>            <span class="n">next_tech</span><span class="p">[</span><span class="n">user</span><span class="o">.</span><span class="n">get_id</span><span class="p">()]</span> <span class="o">=</span> <span class="n">user</span><span class="o">.</span><span class="n">choose_tech</span><span class="p">()</span>
<a name="cl-96"></a>        
<a name="cl-97"></a>        <span class="c">#THEN we apply the new technology choices across all users</span>
<a name="cl-98"></a>        <span class="k">for</span> <span class="n">user</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="o">.</span><span class="n">values</span><span class="p">():</span> <span class="c">#Iterating over User objects</span>
<a name="cl-99"></a>            <span class="n">user</span><span class="o">.</span><span class="n">set_tech</span><span class="p">(</span><span class="n">next_tech</span><span class="p">[</span><span class="n">user</span><span class="o">.</span><span class="n">get_id</span><span class="p">()])</span>
<a name="cl-100"></a>        
<a name="cl-101"></a>    <span class="k">def</span> <span class="nf">get_users</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-102"></a>        <span class="sd">&quot;&quot;&quot;returns a list containing the users in the graph, in</span>
<a name="cl-103"></a><span class="sd">        order of their IDs&quot;&quot;&quot;</span>
<a name="cl-104"></a>        <span class="k">return</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">users</span><span class="o">.</span><span class="n">values</span><span class="p">())</span> <span class="c">#Uses User class comparison</span>
<a name="cl-105"></a>
<a name="cl-106"></a>    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-107"></a>        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">get_users</span><span class="p">())</span>
<a name="cl-108"></a>
<a name="cl-109"></a><span class="k">class</span> <span class="nc">User</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span> <span class="c">#represent a single person in the graph</span>
<a name="cl-110"></a>    
<a name="cl-111"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">ID</span><span class="p">):</span>
<a name="cl-112"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ID</span> <span class="o">=</span> <span class="n">ID</span>
<a name="cl-113"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">friends</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span> <span class="c">#A &quot;set&quot; automatically avoids duplications</span>
<a name="cl-114"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tech</span> <span class="o">=</span> <span class="bp">None</span> <span class="c">#Start out in &quot;low-tech&quot; state :)</span>
<a name="cl-115"></a>    
<a name="cl-116"></a>    <span class="k">def</span> <span class="nf">__lt__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
<a name="cl-117"></a>        <span class="sd">&quot;&quot;&quot;this is a built in comparison function, so that</span>
<a name="cl-118"></a><span class="sd">        user1 &lt; user2 always returns False.  You may not need</span>
<a name="cl-119"></a><span class="sd">        this method at all, but it can sometimes be handy</span>
<a name="cl-120"></a><span class="sd">        for sorting lists that contain users without throwing</span>
<a name="cl-121"></a><span class="sd">        errors&quot;&quot;&quot;</span>
<a name="cl-122"></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">ID</span> <span class="o">&lt;</span> <span class="n">other</span><span class="o">.</span><span class="n">ID</span> <span class="c">#We assume id is unique</span>
<a name="cl-123"></a>    
<a name="cl-124"></a>    <span class="k">def</span> <span class="nf">get_friends</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-125"></a>        <span class="sd">&quot;&quot;&quot;returns a list of the user&#39;s friends,</span>
<a name="cl-126"></a><span class="sd">        which are also users&quot;&quot;&quot;</span>
<a name="cl-127"></a>        <span class="k">return</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">friends</span><span class="p">)</span> <span class="c">#Sorted always makes a list</span>
<a name="cl-128"></a>        
<a name="cl-129"></a>    <span class="k">def</span> <span class="nf">get_id_of_friends</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-130"></a>        <span class="sd">&quot;&quot;&quot;returns a list of the user&#39;s friends&#39; IDs&quot;&quot;&quot;</span>
<a name="cl-131"></a>        <span class="n">id_list</span><span class="o">=</span><span class="p">[]</span>
<a name="cl-132"></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">friends</span><span class="p">):</span>
<a name="cl-133"></a>            <span class="n">id_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">i</span><span class="o">.</span><span class="n">get_id</span><span class="p">())</span>
<a name="cl-134"></a>        <span class="k">return</span> <span class="n">id_list</span>
<a name="cl-135"></a>    
<a name="cl-136"></a>    <span class="k">def</span> <span class="nf">make_friends</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
<a name="cl-137"></a>        <span class="sd">&quot;&quot;&quot;Add friendship link symmetrically between two User objects&quot;&quot;&quot;</span>
<a name="cl-138"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">friends</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">other</span><span class="p">)</span>
<a name="cl-139"></a>        <span class="n">other</span><span class="o">.</span><span class="n">friends</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="c">#Don&#39;t call other.make_friends()</span>
<a name="cl-140"></a>    
<a name="cl-141"></a>    <span class="k">def</span> <span class="nf">is_friend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">other</span><span class="p">):</span>
<a name="cl-142"></a>        <span class="sd">&quot;&quot;&quot;returns True if this User and other are friends.</span>
<a name="cl-143"></a><span class="sd">            returns False otherwise&quot;&quot;&quot;</span>
<a name="cl-144"></a>        <span class="k">return</span> <span class="n">other</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">friends</span>
<a name="cl-145"></a>
<a name="cl-146"></a>    <span class="k">def</span> <span class="nf">get_id</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-147"></a>        <span class="sd">&quot;&quot;&quot;Returns this User&#39;s id&quot;&quot;&quot;</span>
<a name="cl-148"></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">ID</span>
<a name="cl-149"></a>
<a name="cl-150"></a>    <span class="k">def</span> <span class="nf">get_tech</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-151"></a>        <span class="sd">&quot;&quot;&quot;Returns the Technology used by the User, or None if</span>
<a name="cl-152"></a><span class="sd">        the User has no Technology&quot;&quot;&quot;</span>
<a name="cl-153"></a>        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tech</span>
<a name="cl-154"></a>
<a name="cl-155"></a>    <span class="k">def</span> <span class="nf">set_tech</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tech</span><span class="p">):</span>
<a name="cl-156"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tech</span> <span class="o">=</span> <span class="n">tech</span>
<a name="cl-157"></a>        
<a name="cl-158"></a>    <span class="k">def</span> <span class="nf">neighboring_tech</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-159"></a>        <span class="sd">&quot;&quot;&quot;Gather the tech each friend using into a list (with duplicates)&quot;&quot;&quot;</span>
<a name="cl-160"></a>        <span class="k">pass</span> <span class="c">#TODO: Write this helper function!!!</span>
<a name="cl-161"></a>    
<a name="cl-162"></a>    <span class="k">def</span> <span class="nf">choose_tech</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-163"></a>        <span class="sd">&quot;&quot;&quot;Adopt most popular tech amongst friends (include self)&quot;&quot;&quot;</span>
<a name="cl-164"></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">friends</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">0</span><span class="p">:</span> <span class="c">#So sad, no friends :(</span>
<a name="cl-165"></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tech</span> <span class="c">#No influences, so no change to our tech</span>
<a name="cl-166"></a>        
<a name="cl-167"></a>        <span class="c">#TODO: Rewrite as simpler &quot;helper function&quot; instead of this MESS!</span>
<a name="cl-168"></a>        <span class="n">tech_influences</span> <span class="o">=</span> <span class="p">[</span><span class="n">f</span><span class="o">.</span><span class="n">tech</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">friends</span><span class="p">]</span>
<a name="cl-169"></a>        <span class="n">tech_influences</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">tech</span><span class="p">)</span> <span class="c">#Our tech is like 1 &quot;vote&quot;</span>
<a name="cl-170"></a>        <span class="n">tech_influences</span> <span class="o">=</span> <span class="p">[</span><span class="n">t</span> <span class="k">for</span> <span class="n">t</span> <span class="ow">in</span> <span class="n">tech_influences</span> <span class="k">if</span> <span class="n">t</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">]</span>
<a name="cl-171"></a>        <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">tech_influences</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
<a name="cl-172"></a>            <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">tech</span> <span class="c">#We are in a low-tech bubble :(</span>
<a name="cl-173"></a>
<a name="cl-174"></a>        <span class="n">tech_set</span> <span class="o">=</span> <span class="nb">set</span><span class="p">(</span><span class="n">tech_influences</span><span class="p">)</span> <span class="c">#Eliminate duplicates</span>
<a name="cl-175"></a>        <span class="n">winner</span> <span class="o">=</span> <span class="bp">None</span>
<a name="cl-176"></a>        <span class="n">highest</span> <span class="o">=</span> <span class="mi">0</span>
<a name="cl-177"></a>        <span class="k">for</span> <span class="n">tech</span> <span class="ow">in</span> <span class="n">tech_set</span><span class="p">:</span>
<a name="cl-178"></a>            <span class="n">tally</span> <span class="o">=</span> <span class="n">tech_influences</span><span class="o">.</span><span class="n">count</span><span class="p">(</span><span class="n">tech</span><span class="p">)</span>
<a name="cl-179"></a>            <span class="c">#TODO: Ensure &quot;random() &lt; 0.5&quot; is ok! ???</span>
<a name="cl-180"></a>            <span class="k">if</span> <span class="n">tally</span><span class="o">&gt;</span><span class="n">highest</span> <span class="ow">or</span> <span class="p">(</span><span class="n">tally</span><span class="o">==</span><span class="n">highest</span> <span class="ow">and</span> <span class="n">random</span><span class="p">()</span><span class="o">&lt;</span><span class="mf">0.5</span><span class="p">):</span>
<a name="cl-181"></a>                <span class="n">highest</span> <span class="o">=</span> <span class="n">tally</span>
<a name="cl-182"></a>                <span class="n">winner</span> <span class="o">=</span> <span class="n">tech</span>
<a name="cl-183"></a>        <span class="c">#Last tech in winner spot has most votes (or beat in tie cases)</span>
<a name="cl-184"></a>        <span class="k">return</span> <span class="n">winner</span> <span class="c">#We just return the winner, don&#39;t set it yet!</span>
<a name="cl-185"></a>      
<a name="cl-186"></a>    <span class="k">def</span> <span class="nf">__repr__</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-187"></a>        <span class="k">return</span> <span class="s">&quot;User(ID={},tech={},num_direct_friends={},direct_friends={})&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span>
<a name="cl-188"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">ID</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">tech</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">friends</span><span class="p">),</span><span class="bp">self</span><span class="o">.</span><span class="n">get_id_of_friends</span><span class="p">())</span>
<a name="cl-189"></a>
<a name="cl-190"></a>
<a name="cl-191"></a><span class="k">class</span> <span class="nc">Technology</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span> <span class="c">#represent 1 company&#39;s product</span>
<a name="cl-192"></a>
<a name="cl-193"></a>    <span class="n">nextID</span> <span class="o">=</span> <span class="mi">0</span> <span class="c">#Class attribute for assigning sequential ID numbers</span>
<a name="cl-194"></a>    
<a name="cl-195"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">label</span><span class="p">,</span> <span class="n">color</span><span class="o">=</span><span class="s">&quot;red&quot;</span><span class="p">):</span>
<a name="cl-196"></a>        <span class="sd">&quot;&quot;&quot;Each technology should be constructed with</span>
<a name="cl-197"></a><span class="sd">        a text label and a color for display purposes&quot;&quot;&quot;</span>
<a name="cl-198"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">label</span> <span class="o">=</span> <span class="n">label</span>
<a name="cl-199"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">color</span> <span class="o">=</span> <span class="n">color</span>
<a name="cl-200"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">ID</span> <span class="o">=</span> <span class="n">Technology</span><span class="o">.</span><span class="n">nextID</span>
<a name="cl-201"></a>        <span class="n">Technology</span><span class="o">.</span><span class="n">nextID</span> <span class="o">+=</span> <span class="mi">1</span>
<a name="cl-202"></a>
<a name="cl-203"></a><span class="k">class</span> <span class="nc">RandomGraphAnalyzer</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-204"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">graph</span><span class="p">,</span> <span class="n">my_tech</span><span class="p">):</span>
<a name="cl-205"></a>        <span class="sd">&quot;&quot;&quot;Construct a new analyzer to study a provided graph,</span>
<a name="cl-206"></a><span class="sd">        where my_tech represents the given company&#39;s technology&quot;&quot;&quot;</span>
<a name="cl-207"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">graph</span> <span class="o">=</span> <span class="n">graph</span>
<a name="cl-208"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tech</span> <span class="o">=</span> <span class="n">my_tech</span>
<a name="cl-209"></a>
<a name="cl-210"></a>    <span class="k">def</span> <span class="nf">choose_user</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-211"></a>        <span class="sd">&quot;&quot;&quot;returns a user that does not currently have</span>
<a name="cl-212"></a><span class="sd">        a technology, to serve as a first-adopter for </span>
<a name="cl-213"></a><span class="sd">        this analyzer&#39;s technology&quot;&quot;&quot;</span>
<a name="cl-214"></a>        <span class="n">user_list</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">get_users</span><span class="p">()</span>
<a name="cl-215"></a>        <span class="n">nontech_users</span> <span class="o">=</span> <span class="p">[</span><span class="n">u</span> <span class="k">for</span> <span class="n">u</span> <span class="ow">in</span> <span class="n">user_list</span> <span class="k">if</span> <span class="n">u</span><span class="o">.</span><span class="n">get_tech</span><span class="p">()</span> <span class="o">==</span> <span class="bp">None</span><span class="p">]</span>
<a name="cl-216"></a>        <span class="n">pick</span> <span class="o">=</span> <span class="n">randrange</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">nontech_users</span><span class="p">))</span>
<a name="cl-217"></a>        <span class="k">return</span> <span class="n">nontech_users</span><span class="p">[</span><span class="n">pick</span><span class="p">]</span>
<a name="cl-218"></a>
<a name="cl-219"></a><span class="k">class</span> <span class="nc">GraphAnalyzer</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-220"></a>        
<a name="cl-221"></a>    <span class="n">max_distance</span> <span class="o">=</span> <span class="mi">5</span>
<a name="cl-222"></a>    
<a name="cl-223"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">graph</span><span class="p">,</span> <span class="n">my_tech</span><span class="p">):</span>
<a name="cl-224"></a>        <span class="sd">&quot;&quot;&quot;Construct a new analyzer to study a provided graph,</span>
<a name="cl-225"></a><span class="sd">        where my_tech represents the given company&#39;s technology&quot;&quot;&quot;</span>
<a name="cl-226"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">graph</span> <span class="o">=</span> <span class="n">graph</span>
<a name="cl-227"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">tech</span> <span class="o">=</span> <span class="n">my_tech</span>
<a name="cl-228"></a>        
<a name="cl-229"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">which_pick</span> <span class="o">=</span> <span class="mi">0</span> <span class="c">#What round of &quot;picking&quot; are we on (everyone gets 3 rounds)</span>
<a name="cl-230"></a>        
<a name="cl-231"></a>        <span class="n">all_users</span> <span class="o">=</span> <span class="n">graph</span><span class="o">.</span><span class="n">get_users</span><span class="p">()</span> <span class="c">#This list of User objects is sorted by user-id already</span>
<a name="cl-232"></a>        <span class="c">#all_UIDs = [u.get_id() for u in all_users] #Pull user-id (int) from each User object</span>
<a name="cl-233"></a>        
<a name="cl-234"></a>        <span class="c">#self.neighborhood = [self.neighborhood_weight(u) for u in all_users]</span>
<a name="cl-235"></a>        
<a name="cl-236"></a>        <span class="c"># Build stats dictionary (key&#39;d by user-id #, values are #-friends at distance 0 thru 5)</span>
<a name="cl-237"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">stat_friend</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">()</span>
<a name="cl-238"></a>        <span class="k">for</span> <span class="n">u</span> <span class="ow">in</span> <span class="n">all_users</span><span class="p">:</span>
<a name="cl-239"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">stat_friend</span><span class="p">[</span><span class="n">u</span><span class="o">.</span><span class="n">get_id</span><span class="p">()]</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span> <span class="c">#New friends at each increasing distance</span>
<a name="cl-240"></a>        <span class="k">for</span> <span class="n">u</span> <span class="ow">in</span> <span class="n">all_users</span><span class="p">:</span>
<a name="cl-241"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">breadthfirst_stats</span><span class="p">(</span><span class="n">u</span><span class="p">,</span> <span class="n">GraphAnalyzer</span><span class="o">.</span><span class="n">max_distance</span><span class="p">)</span>
<a name="cl-242"></a>        
<a name="cl-243"></a>        <span class="c"># Calculate friendship based &quot;score&quot; for all users</span>
<a name="cl-244"></a>        <span class="n">scores</span> <span class="o">=</span> <span class="n">Counter</span><span class="p">()</span> <span class="c">#Scores is the raw &quot;friendship&quot; rating per-user</span>
<a name="cl-245"></a>        <span class="k">for</span> <span class="n">uid</span><span class="p">,</span><span class="n">counts</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">stat_friend</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
<a name="cl-246"></a>            <span class="n">stats</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">counts</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
<a name="cl-247"></a>            <span class="c">#print(stats)</span>
<a name="cl-248"></a>            <span class="n">s</span> <span class="o">=</span> <span class="mi">0</span>
<a name="cl-249"></a>            <span class="n">w</span> <span class="o">=</span> <span class="mi">1</span> <span class="c">#Immediate friend counts as 1 whole friend</span>
<a name="cl-250"></a>            <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">stats</span><span class="p">:</span> <span class="c">#As distance increases</span>
<a name="cl-251"></a>                <span class="n">s</span> <span class="o">+=</span> <span class="n">c</span> <span class="o">*</span> <span class="n">w</span>
<a name="cl-252"></a>                <span class="n">w</span> <span class="o">*=</span> <span class="mf">0.5</span> <span class="c">#Tapers off in half-of-half-of-half</span>
<a name="cl-253"></a>            <span class="n">scores</span><span class="p">[</span><span class="n">uid</span><span class="p">]</span> <span class="o">=</span> <span class="n">s</span>
<a name="cl-254"></a>        <span class="n">max_score</span> <span class="o">=</span> <span class="nb">max</span><span class="p">(</span><span class="n">scores</span><span class="o">.</span><span class="n">values</span><span class="p">())</span>
<a name="cl-255"></a>        
<a name="cl-256"></a>        <span class="c"># Calculate a &quot;normalized&quot; hotness of each user</span>
<a name="cl-257"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">hotness</span> <span class="o">=</span> <span class="n">OrderedDict</span><span class="p">()</span>
<a name="cl-258"></a>        <span class="k">for</span> <span class="n">uid</span><span class="p">,</span><span class="n">score</span> <span class="ow">in</span> <span class="n">scores</span><span class="o">.</span><span class="n">items</span><span class="p">():</span>
<a name="cl-259"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">hotness</span><span class="p">[</span><span class="n">uid</span><span class="p">]</span> <span class="o">=</span> <span class="n">scores</span><span class="p">[</span><span class="n">uid</span><span class="p">]</span> <span class="o">/</span> <span class="n">max_score</span> <span class="c">#Normalize to 0 to 1 range</span>
<a name="cl-260"></a>        
<a name="cl-261"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">sort_friend</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">stat_friend</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="c">#ITEM tuples</span>
<a name="cl-262"></a>                                  <span class="n">key</span><span class="o">=</span><span class="n">GraphAnalyzer</span><span class="o">.</span><span class="n">sort_max_friends</span><span class="p">)</span>
<a name="cl-263"></a><span class="c">##        self.lambda_friend = sorted(self.stat_friend.values(), reverse=True, #VALUES only</span>
<a name="cl-264"></a><span class="c">##                                    key=lambda v:tuple(v))</span>
<a name="cl-265"></a>        
<a name="cl-266"></a>        <span class="k">if</span> <span class="bp">False</span><span class="p">:</span> <span class="c">#DEBUGGING???</span>
<a name="cl-267"></a>            <span class="k">print</span><span class="p">(</span><span class="s">&#39;friend stats:&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">stat_friend</span><span class="p">)</span>
<a name="cl-268"></a>            <span class="k">print</span><span class="p">(</span><span class="s">&#39;sorted stats:&#39;</span><span class="p">,</span> <span class="bp">self</span><span class="o">.</span><span class="n">sort_friend</span><span class="p">)</span>
<a name="cl-269"></a><span class="c">##            print(&#39;lambda stats:&#39;, self.lambda_friend)</span>
<a name="cl-270"></a>        
<a name="cl-271"></a>    <span class="nd">@staticmethod</span> <span class="c">#this method is not specific to one instance</span>
<a name="cl-272"></a>    <span class="k">def</span> <span class="nf">sort_max_friends</span><span class="p">(</span><span class="n">kvpair</span><span class="p">):</span>
<a name="cl-273"></a>        <span class="n">k</span><span class="p">,</span><span class="n">v</span> <span class="o">=</span> <span class="n">kvpair</span> <span class="c">#k is a user, v is our &quot;#-friends at each distance&quot; statistic array</span>
<a name="cl-274"></a>        <span class="k">return</span> <span class="p">(</span><span class="n">v</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">v</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">v</span><span class="p">[</span><span class="mi">2</span><span class="p">],</span> <span class="n">v</span><span class="p">[</span><span class="mi">3</span><span class="p">],</span> <span class="n">v</span><span class="p">[</span><span class="mi">4</span><span class="p">],</span> <span class="n">v</span><span class="p">[</span><span class="mi">5</span><span class="p">])</span> <span class="c">#...or can coerce the list into a tuple</span>
<a name="cl-275"></a>    
<a name="cl-276"></a>    <span class="k">def</span> <span class="nf">breadthfirst_stats</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">base_user</span><span class="p">,</span> <span class="n">max_distance</span><span class="p">):</span>
<a name="cl-277"></a>        <span class="c"># Keep a pointer to the Counter &quot;dict&quot; for base user</span>
<a name="cl-278"></a>        <span class="n">base_stats</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">stat_friend</span><span class="p">[</span><span class="n">base_user</span><span class="o">.</span><span class="n">get_id</span><span class="p">()]</span>
<a name="cl-279"></a>        
<a name="cl-280"></a>        <span class="c"># queue &amp; visited are standard breadth-first search tricks (we use &quot;deque&quot; for efficiency)</span>
<a name="cl-281"></a>        <span class="n">queue</span> <span class="o">=</span> <span class="n">deque</span><span class="p">([(</span><span class="n">base_user</span><span class="p">,</span> <span class="p">())])</span> <span class="c">#Seed the queue with root user and empty chain (zero distance)</span>
<a name="cl-282"></a>        <span class="n">visited</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span> <span class="c">#Visited is the set of nodes/users we have discovered</span>
<a name="cl-283"></a>        
<a name="cl-284"></a>        <span class="k">while</span> <span class="nb">len</span><span class="p">(</span><span class="n">queue</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
<a name="cl-285"></a>            <span class="c"># Manage the queue (standard breadth first algorithm)</span>
<a name="cl-286"></a>            <span class="n">user</span><span class="p">,</span><span class="n">chain</span> <span class="o">=</span> <span class="n">queue</span><span class="o">.</span><span class="n">popleft</span><span class="p">()</span> <span class="c">#Important thing is the user (we also build chains, though)</span>
<a name="cl-287"></a>            
<a name="cl-288"></a>            <span class="c"># Contribute the visited user to the base user&#39;s statistics</span>
<a name="cl-289"></a>            <span class="k">if</span> <span class="ow">not</span> <span class="n">user</span> <span class="ow">in</span> <span class="n">visited</span><span class="p">:</span> <span class="c">#These are the stats for which re-visits are not desired</span>
<a name="cl-290"></a>                <span class="n">base_stats</span><span class="p">[</span><span class="nb">len</span><span class="p">(</span><span class="n">chain</span><span class="p">)]</span> <span class="o">+=</span> <span class="mi">1</span>
<a name="cl-291"></a>                <span class="n">visited</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">user</span><span class="p">)</span> <span class="c">#Remember as visited (is a &quot;set&quot;, so use add()!)</span>
<a name="cl-292"></a>            
<a name="cl-293"></a>            <span class="c"># Are there other stats to pull in? Weights, second-hand info?</span>
<a name="cl-294"></a>            <span class="c"># Important one is what TEAM/tech the user currently has (or None)!</span>
<a name="cl-295"></a>            
<a name="cl-296"></a>            <span class="c">#Could check for for excessively high stats</span>
<a name="cl-297"></a>            <span class="c">#    on this node and decide to skip it&#39;s links!</span>
<a name="cl-298"></a>            <span class="c">#  Or could override standard distance limit based</span>
<a name="cl-299"></a>            <span class="c">#    on stats that are looking very special!</span>
<a name="cl-300"></a>            
<a name="cl-301"></a>            <span class="c"># Advance another step away from base node</span>
<a name="cl-302"></a>            <span class="n">chain</span> <span class="o">+=</span> <span class="p">(</span><span class="n">user</span><span class="p">,)</span> <span class="c">#Append user to the &quot;chain&quot; tuple</span>
<a name="cl-303"></a><span class="c">##            print(&quot;Chain:&quot;, &quot;--&gt;&quot;.join([str(u.get_id()) for u in chain]))</span>
<a name="cl-304"></a>            
<a name="cl-305"></a>            <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">chain</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">max_distance</span><span class="p">:</span>
<a name="cl-306"></a><span class="c">##                print(&quot;TOO FAR: {} &gt; {}&quot;.format(len(chain), max_distance))</span>
<a name="cl-307"></a>                <span class="k">continue</span>
<a name="cl-308"></a>            
<a name="cl-309"></a>            <span class="c"># Explore immediate friends but avoid any &quot;cycles&quot; or &quot;loops&quot; in our path</span>
<a name="cl-310"></a>            <span class="n">lamma_loopers</span> <span class="o">=</span> <span class="p">[</span><span class="n">f</span> <span class="k">for</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">user</span><span class="o">.</span><span class="n">get_friends</span><span class="p">()</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">f</span> <span class="ow">in</span> <span class="n">chain</span><span class="p">]</span>
<a name="cl-311"></a>            <span class="n">queue</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span> <span class="nb">zip</span><span class="p">(</span><span class="n">lamma_loopers</span><span class="p">,</span> <span class="n">repeat</span><span class="p">(</span><span class="n">chain</span><span class="p">))</span> <span class="p">)</span> <span class="c">#Queue up immediate friends w/chain</span>
<a name="cl-312"></a>
<a name="cl-313"></a>    <span class="k">def</span> <span class="nf">neighborhood</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">user</span><span class="p">,</span> <span class="n">distance</span><span class="p">):</span>
<a name="cl-314"></a>        <span class="k">if</span> <span class="n">distance</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="nb">set</span><span class="p">([</span><span class="n">user</span><span class="p">])</span>
<a name="cl-315"></a>        <span class="k">elif</span> <span class="n">distance</span> <span class="o">&lt;</span> <span class="mi">0</span><span class="p">:</span> <span class="k">return</span> <span class="nb">set</span><span class="p">()</span>
<a name="cl-316"></a>        
<a name="cl-317"></a>        <span class="n">neighbors</span> <span class="o">=</span> <span class="nb">set</span><span class="p">([</span><span class="n">user</span><span class="p">])</span>
<a name="cl-318"></a>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="n">user</span><span class="o">.</span><span class="n">get_friends</span><span class="p">():</span><span class="c">#i = immediate friends</span>
<a name="cl-319"></a>            <span class="n">neighbors</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">neighborhood</span><span class="p">(</span><span class="n">i</span><span class="p">,</span> <span class="n">distance</span><span class="o">-</span><span class="mi">1</span><span class="p">))</span>
<a name="cl-320"></a>        <span class="k">return</span> <span class="n">neighbors</span>
<a name="cl-321"></a>    
<a name="cl-322"></a>    <span class="k">def</span> <span class="nf">choose_user</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-323"></a>        <span class="sd">&quot;&quot;&quot;returns a user that does not currently have</span>
<a name="cl-324"></a><span class="sd">        a technology, to serve as a first-adopter for </span>
<a name="cl-325"></a><span class="sd">        this analyzer&#39;s technology&quot;&quot;&quot;</span>
<a name="cl-326"></a>        
<a name="cl-327"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">which_pick</span> <span class="o">+=</span> <span class="mi">1</span>
<a name="cl-328"></a>
<a name="cl-329"></a>        <span class="n">all_users</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">get_users</span><span class="p">()</span>
<a name="cl-330"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">techs_in_graph</span> <span class="o">=</span> <span class="p">[</span><span class="n">u</span><span class="o">.</span><span class="n">get_tech</span><span class="p">()</span> <span class="k">for</span> <span class="n">u</span> <span class="ow">in</span> <span class="n">all_users</span> <span class="k">if</span> <span class="n">u</span><span class="o">.</span><span class="n">get_tech</span><span class="p">()</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">]</span>
<a name="cl-331"></a>        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">which_pick</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
<a name="cl-332"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">place_in_order</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">techs_in_graph</span><span class="p">)</span> <span class="o">+</span> <span class="mi">1</span>
<a name="cl-333"></a>        
<a name="cl-334"></a>        <span class="n">competitor_users</span> <span class="o">=</span> <span class="p">[</span><span class="n">u</span> <span class="k">for</span> <span class="n">u</span> <span class="ow">in</span> <span class="n">all_users</span> <span class="k">if</span> <span class="p">(</span><span class="n">u</span><span class="o">.</span><span class="n">get_tech</span><span class="p">()</span><span class="o">!=</span><span class="bp">None</span> <span class="ow">and</span> <span class="n">u</span><span class="o">.</span><span class="n">get_tech</span><span class="p">()</span><span class="o">!=</span><span class="bp">self</span><span class="o">.</span><span class="n">tech</span><span class="p">)]</span>
<a name="cl-335"></a>        <span class="c">#nontech_users = [u for u in all_users if u.get_tech() == None]</span>
<a name="cl-336"></a>        <span class="c">#</span>
<a name="cl-337"></a>        <span class="c">#def keep_match(x,s): # takes a list of sorted (based on popularity) all_users</span>
<a name="cl-338"></a>        <span class="c">#    return [u for u in x if u in s]</span>
<a name="cl-339"></a>        <span class="c">#</span>
<a name="cl-340"></a>        <span class="c">#def keep_non_match(x,s): # takes a list of sorted (based on popularity) all_users</span>
<a name="cl-341"></a>        <span class="c">#    return [u for u in x if not u in s]</span>
<a name="cl-342"></a>        <span class="c"># </span>
<a name="cl-343"></a>        <span class="c">#popularity_list = [self.graph.convert_id_to_user(t[0]) for t in self.sort_friend]</span>
<a name="cl-344"></a>        <span class="c">#print([u.get_id() for u in popularity_list])</span>
<a name="cl-345"></a>        <span class="c">#popularity_list = keep_match(popularity_list, nontech_users)</span>
<a name="cl-346"></a>        <span class="c">#print([u.get_id() for u in popularity_list])</span>
<a name="cl-347"></a>        <span class="c">#</span>
<a name="cl-348"></a>        <span class="c">#print(&quot;competitors: {}&quot;.format([u.get_id() for u in users_with_competitor_tech]))</span>
<a name="cl-349"></a>        <span class="c">#noncompetitor_list = keep_non_match(popularity_list, users_with_competitor_tech)</span>
<a name="cl-350"></a>        <span class="c">#print(&quot;noncompetitors: {}&quot;.format([u.get_id() for u in noncompetitor_list]))</span>
<a name="cl-351"></a>        <span class="c">#most popular user among users with no technology and no nearby competitor</span>
<a name="cl-352"></a>        <span class="c">#if len(noncompetitor_list)&gt;0:</span>
<a name="cl-353"></a>        <span class="c">#    pick = noncompetitor_list[0]</span>
<a name="cl-354"></a>        <span class="c">#else:</span>
<a name="cl-355"></a>        <span class="c">#    pick = popularity_list[0]</span>
<a name="cl-356"></a>        
<a name="cl-357"></a>        <span class="n">hot</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">hotness</span><span class="o">.</span><span class="n">copy</span><span class="p">()</span> <span class="c">#Make copy of playing board&#39;s &quot;landscape&quot;</span>
<a name="cl-358"></a>        <span class="k">for</span> <span class="n">competitor</span> <span class="ow">in</span> <span class="n">competitor_users</span><span class="p">:</span>
<a name="cl-359"></a>            <span class="k">for</span> <span class="n">dist</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="mi">5</span><span class="p">):</span> <span class="c">#Repeatedly expand the neighborhood size</span>
<a name="cl-360"></a>                <span class="k">for</span> <span class="n">n</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">neighborhood</span><span class="p">(</span><span class="n">competitor</span><span class="p">,</span> <span class="n">dist</span><span class="p">):</span>
<a name="cl-361"></a>                    <span class="n">hot</span><span class="p">[</span><span class="n">n</span><span class="o">.</span><span class="n">get_id</span><span class="p">()]</span> <span class="o">*=</span> <span class="mf">0.90</span> <span class="c">#10% deduction, repeatedly</span>
<a name="cl-362"></a>        <span class="c">#print(&quot;hot:&quot;,hot)</span>
<a name="cl-363"></a>        
<a name="cl-364"></a>        <span class="n">hot_sort</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">hot</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">reverse</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="n">itemgetter</span><span class="p">(</span><span class="mi">1</span><span class="p">))</span>
<a name="cl-365"></a>        <span class="c">#print(&quot;hot_sort:&quot;,hot_sort)</span>
<a name="cl-366"></a>        
<a name="cl-367"></a>        <span class="n">avail_id</span> <span class="o">=</span> <span class="p">[</span><span class="n">u</span><span class="o">.</span><span class="n">get_id</span><span class="p">()</span> <span class="k">for</span> <span class="n">u</span> <span class="ow">in</span> <span class="n">all_users</span> <span class="k">if</span> <span class="n">u</span><span class="o">.</span><span class="n">get_tech</span><span class="p">()</span><span class="o">==</span><span class="bp">None</span><span class="p">]</span>
<a name="cl-368"></a>        <span class="n">hot_avail_id</span> <span class="o">=</span> <span class="p">[</span><span class="n">kv</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">kv</span> <span class="ow">in</span> <span class="n">hot_sort</span> <span class="k">if</span> <span class="n">kv</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="ow">in</span> <span class="n">avail_id</span><span class="p">]</span>
<a name="cl-369"></a>        <span class="k">print</span><span class="p">(</span><span class="s">&quot;hot_avail:&quot;</span><span class="p">,</span><span class="n">hot_avail_id</span><span class="p">)</span>
<a name="cl-370"></a>        <span class="n">top_pick_id</span> <span class="o">=</span> <span class="n">hot_avail_id</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="c">#Sorted reverse, so best is at top</span>
<a name="cl-371"></a>        <span class="k">return</span> <span class="n">all_users</span><span class="p">[</span><span class="n">top_pick_id</span><span class="p">]</span>
<a name="cl-372"></a>
<a name="cl-373"></a><span class="c"># Extra Credit: build a GUI interface for project</span>
<a name="cl-374"></a><span class="c"># Grades will be based on completing all functionality in</span>
<a name="cl-375"></a><span class="c"># the assignment, performance in the competition, and</span>
<a name="cl-376"></a><span class="c"># giving a good presentation</span>
<a name="cl-377"></a>
<a name="cl-378"></a><span class="k">def</span> <span class="nf">testBoard</span><span class="p">(</span><span class="n">population</span><span class="p">,</span> <span class="n">cConnect</span><span class="p">,</span> <span class="n">rConnect</span><span class="p">,</span>
<a name="cl-379"></a>              <span class="n">friendships</span><span class="p">,</span> <span class="n">analyzers</span><span class="p">,</span>
<a name="cl-380"></a>              <span class="n">numPicks</span><span class="p">,</span> <span class="n">numSteps</span><span class="p">,</span> <span class="n">stepDelay</span><span class="p">):</span>
<a name="cl-381"></a>    <span class="n">demo</span> <span class="o">=</span> <span class="n">i155_visual</span><span class="o">.</span><span class="n">Demo</span><span class="p">(</span><span class="n">Graph</span><span class="p">,</span> <span class="n">Technology</span><span class="p">,</span> <span class="n">GraphAnalyzer</span><span class="p">)</span>
<a name="cl-382"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoImaginizer</span><span class="p">()</span>
<a name="cl-383"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoGraph</span><span class="p">(</span><span class="n">population</span><span class="p">,</span> <span class="n">cConnect</span><span class="p">,</span> <span class="n">rConnect</span><span class="p">)</span>
<a name="cl-384"></a>    <span class="n">all_users</span> <span class="o">=</span> <span class="n">demo</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">get_users</span><span class="p">()</span>
<a name="cl-385"></a>    <span class="k">for</span> <span class="n">id1</span><span class="p">,</span><span class="n">id2</span> <span class="ow">in</span> <span class="n">friendships</span><span class="p">:</span>
<a name="cl-386"></a>        <span class="n">buddy1</span> <span class="o">=</span> <span class="n">demo</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">convert_id_to_user</span><span class="p">(</span><span class="n">id1</span><span class="p">)</span>
<a name="cl-387"></a>        <span class="n">buddy2</span> <span class="o">=</span> <span class="n">demo</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">convert_id_to_user</span><span class="p">(</span><span class="n">id2</span><span class="p">)</span>
<a name="cl-388"></a>        <span class="n">buddy1</span><span class="o">.</span><span class="n">make_friends</span><span class="p">(</span><span class="n">buddy2</span><span class="p">)</span>
<a name="cl-389"></a>    <span class="c">#print(all_users)</span>
<a name="cl-390"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoTeams</span><span class="p">(</span><span class="n">analyzers</span><span class="p">)</span>
<a name="cl-391"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoTournament</span><span class="p">(</span><span class="n">numPicks</span><span class="p">,</span> <span class="n">numSteps</span><span class="p">,</span> <span class="n">stepDelay</span><span class="p">)</span>
<a name="cl-392"></a>
<a name="cl-393"></a><span class="k">if</span> <span class="bp">False</span><span class="p">:</span>
<a name="cl-394"></a>    <span class="c">#Test Case 0</span>
<a name="cl-395"></a>    <span class="n">testBoard</span><span class="p">(</span><span class="n">population</span><span class="o">=</span><span class="mi">12</span><span class="p">,</span><span class="n">cConnect</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">rConnect</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
<a name="cl-396"></a>              <span class="n">friendships</span><span class="o">=</span><span class="p">((</span><span class="mi">9</span><span class="p">,</span><span class="mi">5</span><span class="p">),</span> <span class="p">(</span><span class="mi">6</span><span class="p">,</span><span class="mi">1</span><span class="p">),</span> <span class="p">(</span><span class="mi">7</span><span class="p">,</span><span class="mi">0</span><span class="p">),</span> <span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="mi">4</span><span class="p">)))</span>
<a name="cl-397"></a>
<a name="cl-398"></a><span class="k">if</span> <span class="bp">False</span><span class="p">:</span>
<a name="cl-399"></a>    <span class="c">#Test &quot;Direct&quot;</span>
<a name="cl-400"></a>    <span class="n">testBoard</span><span class="p">(</span><span class="n">population</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span><span class="n">cConnect</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">rConnect</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
<a name="cl-401"></a>              <span class="n">friendships</span><span class="o">=</span><span class="p">((</span><span class="mi">19</span><span class="p">,</span><span class="mi">17</span><span class="p">),</span> <span class="p">(</span><span class="mi">19</span><span class="p">,</span><span class="mi">16</span><span class="p">),</span> <span class="p">(</span><span class="mi">19</span><span class="p">,</span><span class="mi">15</span><span class="p">),</span> <span class="p">(</span><span class="mi">19</span><span class="p">,</span><span class="mi">7</span><span class="p">),</span> 
<a name="cl-402"></a>                           <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">12</span><span class="p">),</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">10</span><span class="p">),</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">11</span><span class="p">)),</span>
<a name="cl-403"></a>              <span class="n">analyzers</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
<a name="cl-404"></a>              <span class="n">numPicks</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">numSteps</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">stepDelay</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
<a name="cl-405"></a>    <span class="c">#User-3 already occupied, then Expect: 19</span>
<a name="cl-406"></a>    <span class="c">#User-19 already occupied, then Expect: 8</span>
<a name="cl-407"></a>    
<a name="cl-408"></a><span class="k">if</span> <span class="bp">False</span><span class="p">:</span>
<a name="cl-409"></a>    <span class="c">#Test &quot;Indirect&quot;</span>
<a name="cl-410"></a>    <span class="n">testBoard</span><span class="p">(</span><span class="n">population</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span><span class="n">cConnect</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span><span class="n">rConnect</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
<a name="cl-411"></a>              <span class="n">friendships</span><span class="o">=</span><span class="p">((</span><span class="mi">19</span><span class="p">,</span><span class="mi">17</span><span class="p">),</span> <span class="p">(</span><span class="mi">19</span><span class="p">,</span><span class="mi">16</span><span class="p">),</span> <span class="p">(</span><span class="mi">19</span><span class="p">,</span><span class="mi">15</span><span class="p">),</span>
<a name="cl-412"></a>                           <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">12</span><span class="p">),</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">10</span><span class="p">),</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">11</span><span class="p">),</span>
<a name="cl-413"></a>                           <span class="p">(</span><span class="mi">12</span><span class="p">,</span><span class="mi">5</span><span class="p">),</span> <span class="p">(</span><span class="mi">12</span><span class="p">,</span><span class="mi">6</span><span class="p">)),</span>
<a name="cl-414"></a>              <span class="n">analyzers</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
<a name="cl-415"></a>              <span class="n">numPicks</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">numSteps</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span> <span class="n">stepDelay</span><span class="o">=</span><span class="mi">5</span><span class="p">)</span>
<a name="cl-416"></a>    <span class="c">#Expect: #8</span>
<a name="cl-417"></a>    
<a name="cl-418"></a><span class="k">if</span> <span class="bp">False</span><span class="p">:</span> <span class="c">#Tiny board...only 8 users in a &quot;ring&quot; with 4 randoms</span>
<a name="cl-419"></a>    <span class="n">demo</span> <span class="o">=</span> <span class="n">i155_visual</span><span class="o">.</span><span class="n">Demo</span><span class="p">(</span><span class="n">Graph</span><span class="p">,</span> <span class="n">Technology</span><span class="p">,</span> <span class="n">GraphAnalyzer</span><span class="p">)</span>
<a name="cl-420"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">quickDemo</span><span class="p">(</span><span class="n">population</span><span class="o">=</span><span class="mi">8</span><span class="p">,</span> <span class="n">cConnect</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">rConnect</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
<a name="cl-421"></a>                   <span class="n">numPicks</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">numSteps</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span> <span class="n">stepDelay</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
<a name="cl-422"></a>
<a name="cl-423"></a><span class="k">if</span> <span class="bp">False</span><span class="p">:</span> <span class="c">#Medium board...50 users, circlecon 3, 20 randoms</span>
<a name="cl-424"></a>    <span class="n">demo</span> <span class="o">=</span> <span class="n">i155_visual</span><span class="o">.</span><span class="n">Demo</span><span class="p">(</span><span class="n">Graph</span><span class="p">,</span> <span class="n">Technology</span><span class="p">,</span> <span class="n">GraphAnalyzer</span><span class="p">)</span>
<a name="cl-425"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">quickDemo</span><span class="p">(</span><span class="n">population</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span> <span class="n">cConnect</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">rConnect</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span>
<a name="cl-426"></a>                   <span class="n">numPicks</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">numSteps</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">stepDelay</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<a name="cl-427"></a>
<a name="cl-428"></a><span class="k">if</span> <span class="bp">False</span><span class="p">:</span> <span class="c">#Full tournament board 500 users, circlecon 3, 50 random</span>
<a name="cl-429"></a>    <span class="n">demo</span> <span class="o">=</span> <span class="n">i155_visual</span><span class="o">.</span><span class="n">Demo</span><span class="p">(</span><span class="n">Graph</span><span class="p">,</span> <span class="n">Technology</span><span class="p">,</span> <span class="n">GraphAnalyzer</span><span class="p">)</span>
<a name="cl-430"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">quickDemo</span><span class="p">(</span><span class="n">population</span><span class="o">=</span><span class="mi">500</span><span class="p">,</span> <span class="n">cConnect</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">rConnect</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
<a name="cl-431"></a>                   <span class="n">numPicks</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">numSteps</span><span class="o">=</span><span class="mi">1000</span><span class="p">,</span> <span class="n">stepDelay</span><span class="o">=</span><span class="mf">0.25</span><span class="p">)</span>
<a name="cl-432"></a>
<a name="cl-433"></a><span class="k">if</span> <span class="bp">True</span><span class="p">:</span> <span class="c">#Temporary hotness code (will move into a function/graph later)</span>
<a name="cl-434"></a>    <span class="n">demo</span> <span class="o">=</span> <span class="n">i155_visual</span><span class="o">.</span><span class="n">Demo</span><span class="p">(</span><span class="n">Graph</span><span class="p">,</span> <span class="n">Technology</span><span class="p">,</span> <span class="n">GraphAnalyzer</span><span class="p">)</span>
<a name="cl-435"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoImaginizer</span><span class="p">(</span><span class="n">zigzag</span><span class="o">=</span><span class="mi">8</span><span class="p">)</span>
<a name="cl-436"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoGraph</span><span class="p">(</span><span class="n">population</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">cConnect</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">rConnect</span><span class="o">=</span><span class="mi">50</span><span class="p">)</span>
<a name="cl-437"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoTeams</span><span class="p">()</span>
<a name="cl-438"></a>    <span class="n">g</span> <span class="o">=</span> <span class="n">demo</span><span class="o">.</span><span class="n">graph</span>
<a name="cl-439"></a>    <span class="n">ga</span> <span class="o">=</span> <span class="n">GraphAnalyzer</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">demo</span><span class="o">.</span><span class="n">teams</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span>
<a name="cl-440"></a>    <span class="n">all_users</span> <span class="o">=</span> <span class="n">g</span><span class="o">.</span><span class="n">get_users</span><span class="p">()</span>
<a name="cl-441"></a>    <span class="k">for</span> <span class="n">u</span> <span class="ow">in</span> <span class="n">all_users</span><span class="p">:</span>
<a name="cl-442"></a>        <span class="n">uid</span> <span class="o">=</span> <span class="n">u</span><span class="o">.</span><span class="n">get_id</span><span class="p">()</span>
<a name="cl-443"></a>        <span class="n">c</span> <span class="o">=</span> <span class="n">ga</span><span class="o">.</span><span class="n">hotness</span><span class="p">[</span><span class="n">uid</span><span class="p">]</span>
<a name="cl-444"></a>        <span class="n">all_users</span><span class="p">[</span><span class="n">uid</span><span class="p">]</span><span class="o">.</span><span class="n">hotColor</span> <span class="o">=</span> <span class="p">(</span><span class="n">c</span><span class="p">,</span><span class="n">c</span><span class="p">,</span><span class="n">c</span><span class="p">)</span>
<a name="cl-445"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">imagine</span><span class="o">.</span><span class="n">drawGraph</span><span class="p">(</span><span class="n">g</span><span class="p">,</span> <span class="n">hotOrNot</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
<a name="cl-446"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">imagine</span><span class="o">.</span><span class="n">done</span><span class="p">()</span>
<a name="cl-447"></a>
<a name="cl-448"></a><span class="k">if</span> <span class="bp">False</span><span class="p">:</span> <span class="c">#Head-to-head competition (each strategy type competes)</span>
<a name="cl-449"></a>    <span class="n">demo</span> <span class="o">=</span> <span class="n">i155_visual</span><span class="o">.</span><span class="n">Demo</span><span class="p">(</span><span class="n">Graph</span><span class="p">,</span> <span class="n">Technology</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span>
<a name="cl-450"></a>    <span class="n">analyzers</span><span class="o">=</span><span class="p">[</span><span class="n">GraphAnalyzer</span><span class="p">(</span><span class="n">demo</span><span class="o">.</span><span class="n">graph</span><span class="p">,</span> <span class="n">demo</span><span class="o">.</span><span class="n">teams</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">]),</span> 
<a name="cl-451"></a>               <span class="n">GraphAnalyzer</span><span class="p">(</span><span class="n">demo</span><span class="o">.</span><span class="n">graph</span><span class="p">,</span> <span class="n">demo</span><span class="o">.</span><span class="n">teams</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">1</span><span class="p">])]</span>
<a name="cl-452"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoImaginizer</span><span class="p">(</span><span class="n">zigzag</span><span class="o">=</span><span class="mi">10</span><span class="p">)</span>
<a name="cl-453"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoGraph</span><span class="p">(</span><span class="n">population</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span> <span class="n">cConnect</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">rConnect</span><span class="o">=</span><span class="mi">20</span><span class="p">)</span>
<a name="cl-454"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoTeams</span><span class="p">(</span><span class="n">analyzers</span><span class="p">)</span>
<a name="cl-455"></a>    <span class="n">demo</span><span class="o">.</span><span class="n">demoTournament</span><span class="p">(</span><span class="n">numPicks</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span> <span class="n">numSteps</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">stepDelay</span><span class="o">=</span><span class="mf">0.25</span><span class="p">)</span>
</pre></div>
</td></tr></table>
                </div>
              
            
          
        
      </div>
    </div>
  



<div class="mask"></div>



  <script id="branch-dialog-template" type="text/html">
  

<div class="tabbed-filter-widget branch-dialog">
  <div class="tabbed-filter">
    <input placeholder="Filter branches" class="filter-box" autosave="branch-dropdown-3439168" type="text">
    [[^ignoreTags]]
      <div class="aui-tabs horizontal-tabs aui-tabs-disabled filter-tabs">
        <ul class="tabs-menu">
          <li class="menu-item active-tab"><a href="#branches">Branches</a></li>
          <li class="menu-item"><a href="#tags">Tags</a></li>
        </ul>
      </div>
    [[/ignoreTags]]
  </div>
  
    <div class="tab-pane active-pane" id="branches" data-filter-placeholder="Filter branches">
      <ol class="filter-list">
        <li class="empty-msg">No matching branches</li>
        [[#branches]]
          
            [[#hasMultipleHeads]]
              [[#heads]]
                <li class="comprev filter-item">
                  <a class="pjax-trigger" href="/cdr4eelz/foodie/src/[[changeset]]/final_team_1.py?at=[[safeName]]"
                     title="[[name]]">
                    [[name]] ([[shortChangeset]])
                  </a>
                </li>
              [[/heads]]
            [[/hasMultipleHeads]]
            [[^hasMultipleHeads]]
              <li class="comprev filter-item">
                <a class="pjax-trigger" href="/cdr4eelz/foodie/src/[[changeset]]/final_team_1.py?at=[[safeName]]" title="[[name]]">
                  [[name]]
                </a>
              </li>
            [[/hasMultipleHeads]]
          
        [[/branches]]
      </ol>
    </div>
    <div class="tab-pane" id="tags" data-filter-placeholder="Filter tags">
      <ol class="filter-list">
        <li class="empty-msg">No matching tags</li>
        [[#tags]]
          <li class="comprev filter-item">
            <a class="pjax-trigger" href="/cdr4eelz/foodie/src/[[changeset]]/final_team_1.py?at=[[safeName]]" title="[[name]]">
              [[name]]
            </a>
          </li>
        [[/tags]]
      </ol>
    </div>
  
</div>

</script>



  </div>

  </div>
  

<form id="file-search-form" action="#"
  
  data-revision="6e9f7208836615a94d00ac0a552cbd0dc9881b63"
  data-branch="master">
  <input type="text" id="file-search-query" class="loading">
  <div id="filtered-files"></div>
  <div class="tip"><em>Tip:</em> Filter by directory path e.g. <strong>/media app.js</strong> to search for public<strong>/media/app.js</strong>.</div>
  <div class="tip"><em>Tip:</em> Use camelCasing e.g. <strong>ProjME</strong> to search for <strong>ProjectModifiedE</strong>vent.java.</div>
  <div class="tip"><em>Tip:</em> Filter by extension type e.g. <strong>/repo .js</strong> to search for all <strong>.js</strong> files in the <strong>/repo</strong> directory.</div>
  <div class="tip"><em>Tip:</em> Separate your search with spaces e.g. <strong>/ssh pom.xml</strong> to search for src<strong>/ssh/pom.xml</strong>.</div>
  <div class="tip"><em>Tip:</em> Use ↑ and ↓ arrow keys to navigate and <strong>return</strong> to view the file.</div>
  <div class="tip mod-osx"><em>Tip:</em> You can also navigate files with <strong>Ctrl+j</strong> <em>(next)</em> and <strong>Ctrl+k</strong> <em>(previous)</em> and view the file with <strong>Ctrl+o</strong>.</div>
  <div class="tip mod-win"><em>Tip:</em> You can also navigate files with <strong>Alt+j</strong> <em>(next)</em> and <strong>Alt+k</strong> <em>(previous)</em> and view the file with <strong>Alt+o</strong>.</div>
  <script id="filtered-files-template" type="text/html">
  

<table class="aui bb-list">
  <thead>
    <tr class="assistive">
      <th class="name">Filename</th>
    </tr>
  </thead>
  <tbody>
    [[#files]]
    <tr class="iterable-item">
      <td class="name [[#isDirectory]]directory[[/isDirectory]]">
        <span class="aui-icon aui-icon-small[[#isDirectory]] aui-iconfont-devtools-folder-closed[[/isDirectory]][[^isDirectory]] aui-iconfont-devtools-file[[/isDirectory]]"></span>
        <a href="/cdr4eelz/foodie/src/[[node]]/[[name]][[#branch]]?at=[[branch]][[/branch]]"
           title="[[name]]" class="execute" tabindex="-1">
          [[&highlightedName]]
        </a>
      </td>
    </tr>
    [[/files]]
  </tbody>
</table>

</script>
</form>


    </div>
  </div>

  <footer id="footer" role="contentinfo">
    <section class="footer-body">
      
  <ul>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="Blog"
           href="http://blog.bitbucket.org">Blog</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="Home"
           href="/support">Support</a>
    </li>
    <li>
      <a class="support-ga"
           data-support-gaq-page="PlansPricing"
           href="/plans">Plans &amp; pricing</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="DocumentationHome"
           href="//confluence.atlassian.com/display/BITBUCKET">Documentation</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="DocumentationAPI"
           href="//confluence.atlassian.com/x/IYBGDQ">API</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="SiteStatus"
           href="http://status.bitbucket.org/">Server status</a>
    </li>
    <li>
      <a class="support-ga" id="meta-info"
           data-support-gaq-page="MetaInfo"
           href="#">Version info</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="EndUserAgreement"
           href="//www.atlassian.com/end-user-agreement?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=footer">Terms of service</a>
    </li>
    <li>
      <a class="support-ga" target="_blank"
           data-support-gaq-page="PrivacyPolicy"
           href="//www.atlassian.com/company/privacy?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=footer">Privacy policy</a>
    </li>
  </ul>
  <div id="meta-info-content" style="display: none;">
    <ul>
      
        
          <li><a href="/account/user/fionaroni/"
                 class="view-language-link">English</a></li>
        
      
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="GitDocumentation"
           href="http://git-scm.com/">Git 1.8.2.3</a>
      </li>
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="HgDocumentation"
           href="http://mercurial.selenic.com/">Mercurial 2.2.2</a>
      </li>
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="DjangoDocumentation"
           href="https://www.djangoproject.com/">Django 1.3.7</a>
      </li>
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="PythonDocumentation"
           href="http://www.python.org/">Python 2.7.3</a>
      </li>
      <li>
        <a class="support-ga" target="_blank"
           data-support-gaq-page="DeployedVersion"
           href="#">f908276e9831 / 775588465b77 @ app01</a>
      </li>
    </ul>
  </div>
  <ul class="atlassian-links">
    <li>
      <a id="atlassian-jira-link" target="_blank" title="Track everything – bugs, tasks, deadlines, code – and pull reports to stay informed."
         href="http://www.atlassian.com/software/jira?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">JIRA</a>
    </li>
    <li>
      <a id="atlassian-confluence-link" target="_blank" title="Content Creation, Collaboration & Knowledge Sharing for Teams."
         href="http://www.atlassian.com/software/confluence/overview/team-collaboration-software?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">Confluence</a>
    </li>
    <li>
      <a id="atlassian-bamboo-link" target="_blank" title="Continuous integration and deployment, release management."
         href="http://www.atlassian.com/software/bamboo/overview?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">Bamboo</a>
    </li>
    <li>
      <a id="atlassian-stash-link" target="_blank" title="Git repo management, behind your firewall and Enterprise-ready."
         href="http://www.atlassian.com/software/stash/overview?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">Stash</a>
    </li>
    <li>
      <a id="atlassian-sourcetree-link" target="_blank" title="A free Git and Mercurial desktop client for Mac or Windows."
         href="http://www.sourcetreeapp.com/?utm_source=bitbucket&amp;utm_medium=link&amp;utm_campaign=bitbucket_footer">SourceTree</a>
    </li>
  </ul>
  <div id="footer-logo">
    <a target="_blank" title="Bitbucket is developed by Atlassian in San Francisco."
       href="http://www.atlassian.com?utm_source=bitbucket&amp;utm_medium=logo&amp;utm_campaign=bitbucket_footer">Atlassian</a>
  </div>

    </section>
  </footer>
</div>


  
  <script id="require-js"
          src="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/amd/build/main.js"
          data-main="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/amd/build/main"
          data-page-module="repo/index"></script>




<script>
  (function () {
    var ga = document.createElement('script');
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    ga.setAttribute('async', 'true');
    document.documentElement.firstChild.appendChild(ga);
  }());
</script>

<script>
  setTimeout(function () {
    BB.JsLoaded = true;
  }, 3000);
</script>


  

<script id="source-changeset" type="text/html">
  

<a href="/cdr4eelz/foodie/src/[[raw_node]]/[[path]]?at=master"
   class="[[#selected]]highlight[[/selected]]"
   data-hash="[[node]]">
  [[#author.username]]
    <img class="avatar avatar16" src="[[author.avatar]]"/>
    <span class="author" title="[[raw_author]]">[[author.display_name]]</span>
  [[/author.username]]
  [[^author.username]]
    <img class="avatar avatar16" src="https://d3oaxc4q5k2d6q.cloudfront.net/m/775588465b77/img/default_avatar/16/user_blue.png"/>
    <span class="author unmapped" title="[[raw_author]]">[[author]]</span>
  [[/author.username]]
  <time datetime="[[utctimestamp]]" data-title="true">[[utctimestamp]]</time>
  <span class="message">[[message]]</span>
</a>

</script>
<script id="embed-template" type="text/html">
  

<form class="aui embed">
  <label for="embed-code">Embed this source in another page:</label>
  <input type="text" readonly="true" value="&lt;script src=&quot;[[url]]&quot;&gt;&lt;/script&gt;" id="embed-code">
</form>

</script>
<script id="edit-form-template" type="text/html">
  


<form class="edit-form aui"
      data-repository="[[owner]]/[[slug]]"
      data-destination-repository="[[destinationOwner]]/[[destinationSlug]]"
      data-local-id="[[localID]]"
      data-is-writer="[[#isWriter]]true[[/isWriter]][[^isWriter]]false[[/isWriter]]"
      data-has-push-access="[[#hasPushAccess]]true[[/hasPushAccess]][[^hasPushAccess]]false[[/hasPushAccess]]"
      data-is-pull-request="[[#isPullRequest]]true[[/isPullRequest]][[^isPullRequest]]false[[/isPullRequest]]"
      data-hash="[[hash]]"
      data-branch="[[branch]]"
      data-path="[[path]]"
      data-preview-url="/xhr/[[owner]]/[[slug]]/preview/[[hash]]/[[encodedPath]]"
      data-preview-error="We had trouble generating your preview."
      data-unsaved-changes-error="Your changes will be lost. Are you sure you want to leave?">
  <div class="toolbar clearfix">
    <div class="primary">
      <h2>
        
          Editing <strong>[[path]]</strong> on branch: <strong>[[branch]]</strong>
        
      </h2>
    </div>
    <div class="secondary">
      <div class="hunk-nav aui-buttons">
        <button class="prev-hunk-button aui-button aui-button aui-style"
              disabled="disabled" aria-disabled="true" title="previous change">&#x25B2;</button>
        <button class="next-hunk-button aui-button aui-button aui-style"
              disabled="disabled" aria-disabled="true" title="next change">&#x25BC;</button>
      </div>
    </div>
  </div>
  <div class="file-editor">
    <textarea id="id_source">[[content]]</textarea>
  </div>
  <div class="preview-pane"></div>
  <div class="toolbar footer-toolbar clearfix">
    <div class="primary">
      <div id="syntax-mode" class="field">
        <label for="id_syntax-mode">Syntax mode:</label>
        <select id="id_syntax-mode">
          [[#syntaxes]]
            <option value="[[#mime]][[mime]][[/mime]][[^mime]][[mode]][[/mime]]">[[label]]</option>
          [[/syntaxes]]
        </select>
      </div>
      <div id="indent-mode" class="field">
        <label for="id_indent-mode">Indent mode:</label>
        <select id="id_indent-mode">
          <option value="tabs">Tabs</option>
          <option value="spaces">Spaces</option>
        </select>
      </div>
      <div id="indent-size" class="field">
        <label for="id_indent-size">Indent size:</label>
        <select id="id_indent-size">
          <option value="2">2</option>
          <option value="4">4</option>
          <option value="8">8</option>
        </select>
      </div>
    </div>
    <div class="secondary">
      <button class="preview-button aui-button aui-style"
              disabled="disabled" aria-disabled="true"
              data-preview-label="View diff"
              data-edit-label="Edit file">View diff</button>
      <button class="save-button aui-button aui-button-primary aui-style"
              disabled="disabled" aria-disabled="true">Commit</button>
      <a class="cancel-link" href="#">Cancel</a>
    </div>
  </div>
</form>

</script>
<script id="commit-form-template" type="text/html">
  

<form class="aui commit-form"
      data-title="Commit changes"
      data-default-message="[[filename]] edited online with Bitbucket"
      data-fork-error="We had trouble creating your fork."
      data-commit-error="We had trouble committing your changes."
      data-pull-request-error="We had trouble creating your pull request."
      data-update-error="We had trouble updating your pull request."
      data-branch-conflict-error="A branch with that name already exists."
      data-forking-message="Forking repository"
      data-committing-message="Committing changes"
      data-merging-message="Branching and merging changes"
      data-creating-pr-message="Creating pull request"
      data-updating-pr-message="Updating pull request"
      data-cta-label="Commit"
      data-cancel-label="Cancel">
  <div class="aui-message error hidden">
    <span class="aui-icon icon-error"></span>
    <span class="message"></span>
  </div>
  [[^isWriter]]
    <div class="aui-message info">
      <span class="aui-icon icon-info"></span>
      <p class="title">
        
          You don't have write access to this repository.
        
      </p>
      <span class="message">
        
          We'll create a fork for your changes and submit a
          pull request back to this repository.
        
      </span>
    </div>
  [[/isWriter]]
  <div class="field-group">
    <label for="id_message">Commit message</label>
    <textarea id="id_message" class="textarea"></textarea>
  </div>
  [[^isPullRequest]]
    [[#isWriter]]
      <fieldset class="group">
        <div class="checkbox">
          [[#hasPushAccess]]
            <input id="id_create-pullrequest" class="checkbox" type="checkbox">
            <label for="id_create-pullrequest">Create a pull request for this change</label>
          [[/hasPushAccess]]
          [[^hasPushAccess]]
            <input id="id_create-pullrequest" class="checkbox" type="checkbox" checked="checked" aria-disabled="true" disabled="true">
            <label for="id_create-pullrequest" title="Branch restrictions do not allow you to update this branch.">Create a pull request for this change</label>
          [[/hasPushAccess]]

        </div>
      </fieldset>
      <div id="pr-fields">
        <div id="branch-name-group" class="field-group">
          <label for="id_branch-name">Branch name</label>
          <input type="text" id="id_branch-name" class="text">
        </div>
        <div id="reviewers-group" class="field-group"
              data-api-url="/cdr4eelz/foodie/pull-request/xhr/reviewer/cdr4eelz/foodie/:reviewer_name">
          <label for="participants">Reviewers</label>
          <select id="participants" name="reviewers" multiple></select>
          <div class="error"></div>
          
        </div>
      </div>
    [[/isWriter]]
  [[/isPullRequest]]
  <button type="submit" id="id_submit">Commit</button>
</form>

</script>
<script id="merge-message-template" type="text/html">
  Merged [[hash]] into [[branch]]

[[message]]

</script>
<script id="commit-merge-error-template" type="text/html">
  



  We had trouble merging your changes. We stored them on the <strong>[[branch]]</strong> branch, so feel free to
  <a href="/[[owner]]/[[slug]]/full-commit/[[hash]]/[[path]]?at=[[encodedBranch]]">view them</a> or
  <a href="#" class="create-pull-request-link">create a pull request</a>.


</script>



<div data-modules="components/mentions/index">
  <script id="mention-result" type="text/html">
  
<img class="avatar avatar24" src="[[avatar_url]]">
[[#display_name]]
  <span class="display-name">[[&display_name]]</span> <small class="username">[[&username]]</small>
[[/display_name]]
[[^display_name]]
  <span class="username">[[&username]]</span>
[[/display_name]]
[[#is_teammate]][[^is_team]]
  <span class="aui-lozenge aui-lozenge-complete aui-lozenge-subtle">teammate</span>
[[/is_team]][[/is_teammate]]

</script>
  <script id="mention-call-to-action" type="text/html">
  
[[^query]]
<li class="bb-typeahead-item">Begin typing to search for a user</li>
[[/query]]
[[#query]]
<li class="bb-typeahead-item">Continue typing to search for a user</li>
[[/query]]

</script>
  <script id="mention-no-results" type="text/html">
  
[[^searching]]
<li class="bb-typeahead-item">Found no matching users for <em>[[query]]</em>.</li>
[[/searching]]
[[#searching]]
<li class="bb-typeahead-item bb-typeahead-searching">Searching for <em>[[query]]</em>.</li>
[[/searching]]

</script>
  
    <div id="recently-mentioned-1507978"
        data-value="[]"></div>
  
</div>


  

<script type="text/javascript">if(!NREUMQ.f){NREUMQ.f=function(){NREUMQ.push(["load",new Date().getTime()]);var e=document.createElement("script");e.type="text/javascript";e.src=(("http:"===document.location.protocol)?"http:":"https:")+"//"+"js-agent.newrelic.com/nr-100.js";document.body.appendChild(e);if(NREUMQ.a)NREUMQ.a();};NREUMQ.a=window.onload;window.onload=NREUMQ.f;};NREUMQ.push(["nrfj","beacon-2.newrelic.com","a2cef8c3d3","1841284","Z11RZxdWW0cEVkYLDV4XdUYLVEFdClsdAAtEWkZQDlJBGgRFQhFMQl1DXFcZQ10AQkFYBFlUVlEXWEJHAA==",0,499,new Date().getTime(),"","","","",""]);</script></body>
</html>
