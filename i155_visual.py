<!DOCTYPE html>
<html lang="en">
<head>
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta charset="utf-8">
  <title>
  cdr4eelz / foodie 
  / source  / i155_visual.py
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
        
          <a href="/cdr4eelz/foodie/src/6e9f72088366/i155_visual.py?at=master"
             class="aui-button aui-style pjax-trigger" aria-pressed="true">
            Source
          </a>
          <a href="/cdr4eelz/foodie/diff/i155_visual.py?diff2=6e9f72088366&at=master"
             class="aui-button aui-style pjax-trigger"
             title="Diff to previous change">
            Diff
          </a>
          <a href="/cdr4eelz/foodie/history-node/6e9f72088366/i155_visual.py?at=master"
             class="aui-button aui-style pjax-trigger">
            History
          </a>
        
      </div>
    </div>
  
  <h1>
    <a href="/cdr4eelz/foodie/src/6e9f72088366?at=master"
       class="pjax-trigger" title="cdr4eelz/foodie at 6e9f72088366">foodie</a> /
    
      
        
          <span>i155_visual.py</span>
        
      
    
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
         data-path="i155_visual.py"
         data-source-url="/api/1.0/repositories/cdr4eelz/foodie/src/6e9f7208836615a94d00ac0a552cbd0dc9881b63/i155_visual.py">
      <div id="source-view" data-modules="repo/source/view-file">
        <div class="toolbar">
          <div class="primary">
            <div class="aui-buttons">
              
                <button id="file-history-trigger" class="aui-button aui-style changeset-info"
                        data-changeset="a5487a0b00f2864c4fd52ef0c9bd8c8030e91588"
                        data-path="i155_visual.py"
                        data-current="6e9f7208836615a94d00ac0a552cbd0dc9881b63">
                  
                     

<img class="avatar avatar16" src="https://secure.gravatar.com/avatar/43296b70eb96643c8b57f5e652940f82?d=https%3A%2F%2Fd3oaxc4q5k2d6q.cloudfront.net%2Fm%2F775588465b77%2Fimg%2Fdefault_avatar%2F16%2Fuser_blue.png&amp;s=16" alt="Erik Rogers avatar" />
<span class="changeset-hash">6e9f720</span>
<time datetime="2013-08-16T17:31:58+00:00" class="timestamp"></time>
<span class="aui-icon-dropdown"></span>

                  
                </button>
              
            </div>
          <a href="/cdr4eelz/foodie/full-commit/6e9f72088366/i155_visual.py" id="full-commit-link"
              title="View full commit 6e9f720">Full commit</a>
          </div>
            <div class="secondary">
              <div class="aui-buttons">
                
                  <a href="/cdr4eelz/foodie/annotate/6e9f7208836615a94d00ac0a552cbd0dc9881b63/i155_visual.py?at=master"
                  class="aui-button aui-style pjax-trigger">Blame</a>
                
                
                <a href="/cdr4eelz/foodie/raw/6e9f7208836615a94d00ac0a552cbd0dc9881b63/i155_visual.py"
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
<a href="#cl-192">192</a></pre></div></td><td class="code"><div class="highlight"><pre><a name="cl-1"></a><span class="c">#import tkinter</span>
<a name="cl-2"></a><span class="kn">import</span> <span class="nn">turtle</span>
<a name="cl-3"></a><span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">sleep</span>
<a name="cl-4"></a>
<a name="cl-5"></a><span class="k">class</span> <span class="nc">GraphImaginizer</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-6"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">canvas</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s">&quot;Social Network&quot;</span><span class="p">,</span> <span class="n">bg</span><span class="o">=</span><span class="s">&quot;orange&quot;</span><span class="p">,</span> <span class="n">zigzag</span><span class="o">=</span><span class="mi">0</span><span class="p">):</span>
<a name="cl-7"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">zigzag</span> <span class="o">=</span> <span class="n">zigzag</span>
<a name="cl-8"></a>        <span class="k">if</span> <span class="n">canvas</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-9"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">screen</span> <span class="o">=</span> <span class="n">turtle</span><span class="o">.</span><span class="n">Screen</span><span class="p">()</span> <span class="c">#Default screen (created for us)</span>
<a name="cl-10"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">screen</span><span class="o">.</span><span class="n">setup</span><span class="p">(</span><span class="n">width</span><span class="o">=</span><span class="mf">0.8</span><span class="p">,</span> <span class="n">height</span><span class="o">=</span><span class="mf">0.8</span><span class="p">,</span> <span class="n">startx</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">starty</span><span class="o">=</span><span class="bp">None</span><span class="p">)</span>
<a name="cl-11"></a>            <span class="c">#minPix = min(self.screen.screensize())</span>
<a name="cl-12"></a>        <span class="k">else</span><span class="p">:</span>
<a name="cl-13"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">screen</span> <span class="o">=</span> <span class="n">turtle</span><span class="o">.</span><span class="n">TurtleScreen</span><span class="p">(</span><span class="n">canvas</span><span class="p">)</span>
<a name="cl-14"></a>        <span class="k">if</span> <span class="n">title</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">screen</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>
<a name="cl-15"></a>        <span class="k">if</span> <span class="n">bg</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span> <span class="bp">self</span><span class="o">.</span><span class="n">screen</span><span class="o">.</span><span class="n">bgcolor</span><span class="p">(</span><span class="n">bg</span><span class="p">)</span>
<a name="cl-16"></a>        <span class="c">#Consider registering a custom &quot;Shape&quot;</span>
<a name="cl-17"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">screen</span><span class="o">.</span><span class="n">setworldcoordinates</span><span class="p">(</span><span class="o">-</span><span class="mi">100</span><span class="p">,</span> <span class="o">-</span><span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">,</span> <span class="mi">100</span><span class="p">)</span>
<a name="cl-18"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">screen</span><span class="o">.</span><span class="n">tracer</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">0</span><span class="p">)</span> <span class="c">#No drawing, no delays (must call update() to see)</span>
<a name="cl-19"></a>        
<a name="cl-20"></a>        <span class="n">t</span> <span class="o">=</span> <span class="n">turtle</span><span class="o">.</span><span class="n">Turtle</span><span class="p">()</span>
<a name="cl-21"></a>        <span class="n">t</span><span class="o">.</span><span class="n">shape</span><span class="p">(</span><span class="s">&#39;circle&#39;</span><span class="p">);</span> <span class="n">t</span><span class="o">.</span><span class="n">shapesize</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">1</span><span class="p">,</span> <span class="mf">0.25</span><span class="p">)</span>
<a name="cl-22"></a>        <span class="n">t</span><span class="o">.</span><span class="n">penup</span><span class="p">();</span> <span class="n">t</span><span class="o">.</span><span class="n">speed</span><span class="p">(</span><span class="mi">0</span><span class="p">);</span> <span class="n">t</span><span class="o">.</span><span class="n">hideturtle</span><span class="p">()</span>
<a name="cl-23"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">turtle</span> <span class="o">=</span> <span class="n">t</span>
<a name="cl-24"></a>        
<a name="cl-25"></a>        <span class="n">t</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">turtle</span><span class="o">.</span><span class="n">clone</span><span class="p">()</span>
<a name="cl-26"></a>        <span class="n">t</span><span class="o">.</span><span class="n">shape</span><span class="p">(</span><span class="s">&#39;arrow&#39;</span><span class="p">)</span>
<a name="cl-27"></a>        <span class="c">#t.showturtle()</span>
<a name="cl-28"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">turtle2</span> <span class="o">=</span> <span class="n">t</span>
<a name="cl-29"></a>        
<a name="cl-30"></a>    <span class="k">def</span> <span class="nf">drawUsers</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">user_list</span><span class="p">,</span> <span class="n">hotOrNot</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
<a name="cl-31"></a>        <span class="sd">&quot;&quot;&quot;Plot users with friendship-lines and tech color&quot;&quot;&quot;</span>
<a name="cl-32"></a>        <span class="c"># Circular style graph eliminates lines cutting through other</span>
<a name="cl-33"></a>        <span class="c">#   users.  It also avoids pretending there is a physical</span>
<a name="cl-34"></a>        <span class="c">#   geometry to the graph that has any inherent meaning.</span>
<a name="cl-35"></a>
<a name="cl-36"></a>        <span class="n">num_users</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">user_list</span><span class="p">)</span>
<a name="cl-37"></a>        <span class="c">#TODO: Delete any abandoned User-Turtles</span>
<a name="cl-38"></a>        
<a name="cl-39"></a>        <span class="n">zig</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">zigzag</span>
<a name="cl-40"></a>        <span class="k">if</span> <span class="n">zig</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-41"></a>            <span class="n">zig</span> <span class="o">=</span> <span class="mi">10</span><span class="o">*</span><span class="n">num_users</span> <span class="o">/</span> <span class="mi">500</span> 
<a name="cl-42"></a>        
<a name="cl-43"></a>        <span class="c"># Create User-Turtles (one each) with label &amp; desired position</span>
<a name="cl-44"></a>        <span class="k">for</span> <span class="n">u</span><span class="p">,</span> <span class="n">user</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">user_list</span><span class="p">):</span>
<a name="cl-45"></a>            <span class="k">try</span><span class="p">:</span>
<a name="cl-46"></a>                <span class="n">t</span> <span class="o">=</span> <span class="n">user</span><span class="o">.</span><span class="n">_turtle</span>
<a name="cl-47"></a>            <span class="k">except</span><span class="p">:</span>
<a name="cl-48"></a>                <span class="n">t</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">turtle</span><span class="o">.</span><span class="n">clone</span><span class="p">()</span>
<a name="cl-49"></a>                <span class="n">t</span><span class="o">.</span><span class="n">setheading</span><span class="p">(</span><span class="mi">180</span> <span class="o">-</span> <span class="p">(</span><span class="n">u</span> <span class="o">*</span> <span class="mi">360</span><span class="o">/</span><span class="n">num_users</span><span class="p">))</span>
<a name="cl-50"></a>                <span class="n">t</span><span class="o">.</span><span class="n">forward</span><span class="p">(</span><span class="mi">65</span> <span class="o">+</span> <span class="p">(</span><span class="n">zig</span> <span class="o">*</span> <span class="p">(</span><span class="n">u</span><span class="o">%</span><span class="mi">3</span><span class="p">)))</span>
<a name="cl-51"></a>                <span class="n">t</span><span class="o">.</span><span class="n">write</span><span class="p">(</span><span class="n">user</span><span class="o">.</span><span class="n">get_id</span><span class="p">(),</span> <span class="bp">False</span><span class="p">,</span> <span class="n">align</span><span class="o">=</span><span class="s">&quot;center&quot;</span><span class="p">)</span>
<a name="cl-52"></a>                <span class="n">t</span><span class="o">.</span><span class="n">backward</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<a name="cl-53"></a>                <span class="n">user</span><span class="o">.</span><span class="n">_pos</span> <span class="o">=</span> <span class="n">t</span><span class="o">.</span><span class="n">position</span><span class="p">()</span>
<a name="cl-54"></a>                <span class="c">#t.forward(3)</span>
<a name="cl-55"></a>                <span class="n">user</span><span class="o">.</span><span class="n">_turtle</span> <span class="o">=</span> <span class="n">t</span>
<a name="cl-56"></a>                
<a name="cl-57"></a>        <span class="k">for</span> <span class="n">user</span> <span class="ow">in</span> <span class="n">user_list</span><span class="p">:</span>
<a name="cl-58"></a>            <span class="k">try</span><span class="p">:</span>
<a name="cl-59"></a>                <span class="n">t</span> <span class="o">=</span> <span class="n">user</span><span class="o">.</span><span class="n">_turtle2</span>
<a name="cl-60"></a>            <span class="k">except</span><span class="p">:</span>
<a name="cl-61"></a>                <span class="n">t</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">turtle2</span><span class="o">.</span><span class="n">clone</span><span class="p">()</span>
<a name="cl-62"></a>                <span class="n">user</span><span class="o">.</span><span class="n">_turtle2</span> <span class="o">=</span> <span class="n">t</span>
<a name="cl-63"></a>            <span class="k">for</span> <span class="n">friend</span> <span class="ow">in</span> <span class="n">user</span><span class="o">.</span><span class="n">get_friends</span><span class="p">():</span>
<a name="cl-64"></a>                <span class="n">t</span><span class="o">.</span><span class="n">penup</span><span class="p">()</span>
<a name="cl-65"></a>                <span class="n">t</span><span class="o">.</span><span class="n">setpos</span><span class="p">(</span><span class="n">user</span><span class="o">.</span><span class="n">_pos</span><span class="p">)</span>
<a name="cl-66"></a>                <span class="n">t</span><span class="o">.</span><span class="n">pendown</span><span class="p">()</span>
<a name="cl-67"></a>                <span class="n">t</span><span class="o">.</span><span class="n">setpos</span><span class="p">(</span><span class="n">friend</span><span class="o">.</span><span class="n">_pos</span><span class="p">)</span>
<a name="cl-68"></a>        
<a name="cl-69"></a>        <span class="c"># Apply color from Technology</span>
<a name="cl-70"></a>        <span class="k">for</span> <span class="n">user</span> <span class="ow">in</span> <span class="n">user_list</span><span class="p">:</span>
<a name="cl-71"></a>            <span class="n">t</span> <span class="o">=</span> <span class="n">user</span><span class="o">.</span><span class="n">_turtle</span>
<a name="cl-72"></a>            <span class="n">t</span><span class="o">.</span><span class="n">clearstamps</span><span class="p">()</span>
<a name="cl-73"></a>            <span class="k">if</span> <span class="n">hotOrNot</span><span class="p">:</span>
<a name="cl-74"></a>                <span class="n">t</span><span class="o">.</span><span class="n">color</span><span class="p">(</span><span class="s">&quot;yellow&quot;</span><span class="p">,</span> <span class="n">user</span><span class="o">.</span><span class="n">hotColor</span><span class="p">)</span>
<a name="cl-75"></a>            <span class="k">else</span><span class="p">:</span>
<a name="cl-76"></a>                <span class="n">tech</span> <span class="o">=</span> <span class="n">user</span><span class="o">.</span><span class="n">get_tech</span><span class="p">()</span>
<a name="cl-77"></a>                <span class="k">if</span> <span class="n">tech</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-78"></a>                    <span class="n">t</span><span class="o">.</span><span class="n">color</span><span class="p">(</span><span class="s">&quot;white&quot;</span><span class="p">,</span> <span class="s">&quot;black&quot;</span><span class="p">)</span>
<a name="cl-79"></a>                <span class="k">else</span><span class="p">:</span>
<a name="cl-80"></a>                    <span class="n">t</span><span class="o">.</span><span class="n">color</span><span class="p">(</span><span class="s">&quot;black&quot;</span><span class="p">,</span> <span class="n">tech</span><span class="o">.</span><span class="n">color</span><span class="p">)</span>
<a name="cl-81"></a>            <span class="n">t</span><span class="o">.</span><span class="n">stamp</span><span class="p">()</span>
<a name="cl-82"></a>            <span class="c">#t.begin_fill(); t.circle(4); t.end_fill()</span>
<a name="cl-83"></a>            <span class="c">#t.dot(16)</span>
<a name="cl-84"></a>        
<a name="cl-85"></a>        <span class="c"># Force the screen to render it&#39;s contents</span>
<a name="cl-86"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">screen</span><span class="o">.</span><span class="n">update</span><span class="p">()</span>
<a name="cl-87"></a>    
<a name="cl-88"></a>    <span class="k">def</span> <span class="nf">drawLegend</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tech_list</span><span class="p">):</span>
<a name="cl-89"></a>        <span class="k">pass</span>
<a name="cl-90"></a><span class="c">#         t = turtle.Turtle()</span>
<a name="cl-91"></a><span class="c">#         t.penup()</span>
<a name="cl-92"></a><span class="c">#         t.setposition(-80, -80)</span>
<a name="cl-93"></a><span class="c">#         for i in range(0,len(tech_list),1):</span>
<a name="cl-94"></a><span class="c">#             tech = tech_list[i]</span>
<a name="cl-95"></a><span class="c">#             print(&quot;Label({})={}&quot;.format(i,tech.label))</span>
<a name="cl-96"></a><span class="c">#             t.write(tech.label,move= True , font=(&quot;Arial&quot;, 12,&quot;bold&quot;))</span>
<a name="cl-97"></a>                
<a name="cl-98"></a>    <span class="k">def</span> <span class="nf">drawGraph</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">graph</span><span class="p">,</span> <span class="n">tech</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span> <span class="n">hotOrNot</span><span class="o">=</span><span class="bp">False</span><span class="p">):</span>
<a name="cl-99"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">drawUsers</span><span class="p">(</span><span class="n">graph</span><span class="o">.</span><span class="n">get_users</span><span class="p">(),</span> <span class="n">hotOrNot</span><span class="p">)</span>
<a name="cl-100"></a>        <span class="k">if</span> <span class="n">tech</span> <span class="o">!=</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-101"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">drawLegend</span><span class="p">(</span><span class="n">tech</span><span class="p">)</span>
<a name="cl-102"></a>        
<a name="cl-103"></a>    <span class="k">def</span> <span class="nf">done</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-104"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">screen</span><span class="o">.</span><span class="n">exitonclick</span><span class="p">()</span>
<a name="cl-105"></a>
<a name="cl-106"></a>
<a name="cl-107"></a><span class="k">class</span> <span class="nc">Demo</span><span class="p">(</span><span class="nb">object</span><span class="p">):</span>
<a name="cl-108"></a>    
<a name="cl-109"></a>    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">yourGraphCLASS</span><span class="p">,</span> <span class="n">yourTechnologyCLASS</span><span class="p">,</span> <span class="n">yourGraphAnalyzerCLASS</span><span class="p">):</span>
<a name="cl-110"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_GRAPH</span> <span class="o">=</span> <span class="n">yourGraphCLASS</span>
<a name="cl-111"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span> <span class="o">=</span> <span class="n">yourTechnologyCLASS</span>
<a name="cl-112"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_ANALYZER</span> <span class="o">=</span> <span class="n">yourGraphAnalyzerCLASS</span>
<a name="cl-113"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">imagine</span> <span class="o">=</span> <span class="bp">None</span>
<a name="cl-114"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">graph</span> <span class="o">=</span> <span class="bp">None</span>
<a name="cl-115"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">teams</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-116"></a>        
<a name="cl-117"></a>    <span class="k">def</span> <span class="nf">setImaginizer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">imagine</span><span class="p">):</span>
<a name="cl-118"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">imagine</span> <span class="o">=</span> <span class="n">imagine</span>
<a name="cl-119"></a>        
<a name="cl-120"></a>    <span class="k">def</span> <span class="nf">setGraph</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">graph</span><span class="p">):</span>
<a name="cl-121"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">graph</span> <span class="o">=</span> <span class="n">graph</span>
<a name="cl-122"></a>        
<a name="cl-123"></a>    <span class="k">def</span> <span class="nf">resetTeams</span><span class="p">(</span><span class="bp">self</span><span class="p">):</span>
<a name="cl-124"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">teams</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-125"></a>        
<a name="cl-126"></a>    <span class="k">def</span> <span class="nf">addTeam</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">tech</span><span class="p">,</span> <span class="n">analyzer</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
<a name="cl-127"></a>        <span class="k">if</span> <span class="n">analyzer</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-128"></a>            <span class="n">analyzer</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_ANALYZER</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="p">,</span> <span class="n">tech</span><span class="p">)</span>
<a name="cl-129"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">teams</span><span class="o">.</span><span class="n">append</span><span class="p">(</span> <span class="p">(</span><span class="n">tech</span><span class="p">,</span> <span class="n">analyzer</span><span class="p">)</span> <span class="p">)</span> <span class="c">#Tuple of tech &amp; analyzer</span>
<a name="cl-130"></a>        
<a name="cl-131"></a>    <span class="k">def</span> <span class="nf">demoImaginizer</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">zigzag</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-132"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">setImaginizer</span><span class="p">(</span><span class="n">GraphImaginizer</span><span class="p">(</span><span class="n">zigzag</span><span class="o">=</span><span class="n">zigzag</span><span class="p">))</span>
<a name="cl-133"></a>        
<a name="cl-134"></a>    <span class="k">def</span> <span class="nf">demoGraph</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">population</span><span class="o">=</span><span class="mi">8</span><span class="p">,</span> <span class="n">cConnect</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">rConnect</span><span class="o">=</span><span class="mi">4</span><span class="p">):</span>
<a name="cl-135"></a>        <span class="n">g</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_GRAPH</span><span class="p">(</span><span class="n">population</span><span class="p">)</span> <span class="c">#Construct instance of student&#39;s Graph()</span>
<a name="cl-136"></a>        <span class="c">#You would just call your Graph() constructor directly!</span>
<a name="cl-137"></a>        <span class="n">g</span><span class="o">.</span><span class="n">circle_connect</span><span class="p">(</span><span class="n">cConnect</span><span class="p">)</span>
<a name="cl-138"></a>        <span class="n">g</span><span class="o">.</span><span class="n">random_connections</span><span class="p">(</span><span class="n">rConnect</span><span class="p">)</span>
<a name="cl-139"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">setGraph</span><span class="p">(</span><span class="n">g</span><span class="p">)</span>
<a name="cl-140"></a>        
<a name="cl-141"></a>    <span class="k">def</span> <span class="nf">demoTeams</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">analyzers</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
<a name="cl-142"></a>        <span class="n">tech_list</span> <span class="o">=</span> <span class="p">[</span><span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team0&#39;</span><span class="p">,</span> <span class="s">&#39;blue&#39;</span><span class="p">),</span>
<a name="cl-143"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team1&#39;</span><span class="p">,</span> <span class="s">&#39;pink&#39;</span><span class="p">),</span>
<a name="cl-144"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team2&#39;</span><span class="p">,</span> <span class="s">&#39;green&#39;</span><span class="p">),</span>
<a name="cl-145"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team3&#39;</span><span class="p">,</span> <span class="s">&#39;yellow&#39;</span><span class="p">),</span>
<a name="cl-146"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team4&#39;</span><span class="p">,</span> <span class="s">&#39;white&#39;</span><span class="p">),</span>
<a name="cl-147"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team5&#39;</span><span class="p">,</span> <span class="s">&#39;red&#39;</span><span class="p">),</span>
<a name="cl-148"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team6&#39;</span><span class="p">,</span> <span class="s">&#39;brown&#39;</span><span class="p">),</span>
<a name="cl-149"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team7&#39;</span><span class="p">,</span> <span class="s">&#39;white&#39;</span><span class="p">),</span>
<a name="cl-150"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team8&#39;</span><span class="p">,</span> <span class="s">&#39;violet&#39;</span><span class="p">),</span>
<a name="cl-151"></a>                     <span class="bp">self</span><span class="o">.</span><span class="n">CLASS_TECH</span><span class="p">(</span><span class="s">&#39;Team9&#39;</span><span class="p">,</span> <span class="s">&#39;gray&#39;</span><span class="p">)]</span>
<a name="cl-152"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">resetTeams</span><span class="p">()</span>
<a name="cl-153"></a>        <span class="k">if</span> <span class="n">analyzers</span> <span class="o">==</span> <span class="bp">None</span><span class="p">:</span>
<a name="cl-154"></a>            <span class="n">analyzers</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">tech_list</span><span class="p">)</span>
<a name="cl-155"></a>        <span class="k">if</span> <span class="nb">type</span><span class="p">(</span><span class="n">analyzers</span><span class="p">)</span> <span class="o">==</span> <span class="nb">int</span><span class="p">:</span>
<a name="cl-156"></a>            <span class="n">analyzers</span> <span class="o">=</span> <span class="p">[</span><span class="bp">None</span><span class="p">]</span> <span class="o">*</span> <span class="n">analyzers</span>
<a name="cl-157"></a>        <span class="k">for</span> <span class="n">tech</span><span class="p">,</span><span class="n">analyze</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">tech_list</span><span class="p">,</span> <span class="n">analyzers</span><span class="p">):</span>
<a name="cl-158"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">addTeam</span><span class="p">(</span><span class="n">tech</span><span class="p">,</span> <span class="n">analyze</span><span class="p">)</span>
<a name="cl-159"></a>    
<a name="cl-160"></a>    <span class="k">def</span> <span class="nf">demoTournament</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">numPicks</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">numSteps</span><span class="o">=</span><span class="mi">10</span><span class="p">,</span> <span class="n">stepDelay</span><span class="o">=</span><span class="mi">3</span><span class="p">):</span>
<a name="cl-161"></a>        <span class="sd">&quot;&quot;&quot;Class method to demonstrate a little drawing action&quot;&quot;&quot;</span>
<a name="cl-162"></a>        
<a name="cl-163"></a>        <span class="n">tech_list</span> <span class="o">=</span> <span class="p">[]</span>
<a name="cl-164"></a>        <span class="k">for</span> <span class="n">team_tech</span><span class="p">,</span> <span class="n">team_analyzer</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">teams</span><span class="p">:</span>
<a name="cl-165"></a>            <span class="n">tech_list</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">team_tech</span><span class="p">)</span>
<a name="cl-166"></a>        
<a name="cl-167"></a>        <span class="c"># Draw legend and graph without initial picks</span>
<a name="cl-168"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">imagine</span><span class="o">.</span><span class="n">drawGraph</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="p">,</span> <span class="n">tech_list</span><span class="p">)</span>
<a name="cl-169"></a>        <span class="n">sleep</span><span class="p">(</span><span class="n">stepDelay</span><span class="p">)</span>
<a name="cl-170"></a>        
<a name="cl-171"></a>        <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">numPicks</span><span class="p">):</span>
<a name="cl-172"></a>            <span class="k">for</span> <span class="n">team_tech</span><span class="p">,</span> <span class="n">team_analyzer</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">teams</span><span class="p">:</span>
<a name="cl-173"></a>                <span class="n">pick_user</span> <span class="o">=</span> <span class="n">team_analyzer</span><span class="o">.</span><span class="n">choose_user</span><span class="p">()</span>
<a name="cl-174"></a>                <span class="k">print</span><span class="p">(</span><span class="s">&quot;{} PICKED {}&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">team_tech</span><span class="o">.</span><span class="n">label</span><span class="p">,</span> <span class="n">pick_user</span><span class="o">.</span><span class="n">get_id</span><span class="p">()))</span>
<a name="cl-175"></a>                <span class="n">pick_user</span><span class="o">.</span><span class="n">set_tech</span><span class="p">(</span><span class="n">team_tech</span><span class="p">)</span>
<a name="cl-176"></a>            <span class="c"># Depict each round of picks</span>
<a name="cl-177"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">imagine</span><span class="o">.</span><span class="n">drawGraph</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="p">)</span>
<a name="cl-178"></a>            <span class="n">sleep</span><span class="p">(</span><span class="n">stepDelay</span><span class="p">)</span>
<a name="cl-179"></a>        
<a name="cl-180"></a>        <span class="k">for</span> <span class="n">_</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">numSteps</span><span class="p">):</span>
<a name="cl-181"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="o">.</span><span class="n">time_step</span><span class="p">()</span>
<a name="cl-182"></a>            <span class="bp">self</span><span class="o">.</span><span class="n">imagine</span><span class="o">.</span><span class="n">drawGraph</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">graph</span><span class="p">)</span>
<a name="cl-183"></a>            <span class="n">sleep</span><span class="p">(</span><span class="n">stepDelay</span><span class="p">)</span>
<a name="cl-184"></a>            
<a name="cl-185"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">imagine</span><span class="o">.</span><span class="n">done</span><span class="p">()</span>
<a name="cl-186"></a>        
<a name="cl-187"></a>    <span class="k">def</span> <span class="nf">quickDemo</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">population</span><span class="o">=</span><span class="mi">15</span><span class="p">,</span> <span class="n">cConnect</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">rConnect</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
<a name="cl-188"></a>                  <span class="n">numPicks</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">numSteps</span><span class="o">=</span><span class="mi">20</span><span class="p">,</span> <span class="n">stepDelay</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span> <span class="n">analyzers</span><span class="o">=</span><span class="bp">None</span><span class="p">):</span>
<a name="cl-189"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">demoImaginizer</span><span class="p">()</span>
<a name="cl-190"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">demoGraph</span><span class="p">(</span><span class="n">population</span><span class="p">,</span> <span class="n">cConnect</span><span class="p">,</span> <span class="n">rConnect</span><span class="p">)</span>
<a name="cl-191"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">demoTeams</span><span class="p">(</span><span class="n">analyzers</span><span class="p">)</span>
<a name="cl-192"></a>        <span class="bp">self</span><span class="o">.</span><span class="n">demoTournament</span><span class="p">(</span><span class="n">numPicks</span><span class="p">,</span> <span class="n">numSteps</span><span class="p">,</span> <span class="n">stepDelay</span><span class="p">)</span>
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
                  <a class="pjax-trigger" href="/cdr4eelz/foodie/src/[[changeset]]/i155_visual.py?at=[[safeName]]"
                     title="[[name]]">
                    [[name]] ([[shortChangeset]])
                  </a>
                </li>
              [[/heads]]
            [[/hasMultipleHeads]]
            [[^hasMultipleHeads]]
              <li class="comprev filter-item">
                <a class="pjax-trigger" href="/cdr4eelz/foodie/src/[[changeset]]/i155_visual.py?at=[[safeName]]" title="[[name]]">
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
            <a class="pjax-trigger" href="/cdr4eelz/foodie/src/[[changeset]]/i155_visual.py?at=[[safeName]]" title="[[name]]">
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
           href="#">f908276e9831 / 775588465b77 @ app07</a>
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


  

<script type="text/javascript">if(!NREUMQ.f){NREUMQ.f=function(){NREUMQ.push(["load",new Date().getTime()]);var e=document.createElement("script");e.type="text/javascript";e.src=(("http:"===document.location.protocol)?"http:":"https:")+"//"+"js-agent.newrelic.com/nr-100.js";document.body.appendChild(e);if(NREUMQ.a)NREUMQ.a();};NREUMQ.a=window.onload;window.onload=NREUMQ.f;};NREUMQ.push(["nrfj","beacon-2.newrelic.com","a2cef8c3d3","1841284","Z11RZxdWW0cEVkYLDV4XdUYLVEFdClsdAAtEWkZQDlJBGgRFQhFMQl1DXFcZQ10AQkFYBFlUVlEXWEJHAA==",0,352,new Date().getTime(),"","","","",""]);</script></body>
</html>
