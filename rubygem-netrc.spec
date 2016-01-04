%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

# Generated from netrc-0.7.gem by gem2rpm -*- rpm-spec -*-
%global gem_name netrc

Summary: Library to read and write netrc files
Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.7.7
Release: 8%{?dist}
Group: Development/Languages
License: MIT
URL: https://github.com/geemus/netrc
Source0: http://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby(rubygems)
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}rubygems-devel
BuildRequires: %{?scl_prefix_ruby}ruby
BuildRequires: %{?scl_prefix_ruby}rubygem(minitest)
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}

%description
This library can read and update netrc files, preserving formatting including
comments and whitespace.

%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}

%prep
%setup -n %{pkg_name}-%{version} -q -c -T
%{?scl:scl enable %{scl} - << \EOF}
%gem_install -n %{SOURCE0}
%{?scl:EOF}

%build

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# To run the tests using minitest 5
%{?scl:scl enable %{scl} - << \EOF}
ruby -rminitest/autorun - << \RUBY
  module Kernel
    alias orig_require require
    remove_method :require

    def require path
      orig_require path unless path == 'test/unit'
    end

  end

  Test = Minitest

  Dir.glob "./test/**/test_*.rb", &method(:require)
RUBY
%{?scl:EOF}
popd

%files
%dir %{gem_instdir}
%doc %{gem_instdir}/LICENSE
%doc %{gem_instdir}/Readme.md
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/changelog.txt
%{gem_instdir}/data
%{gem_instdir}/test

%changelog
* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 0.7.7-8
- Add missing provides

* Thu Feb 19 2015 Josef Stribny <jstribny@redhat.com> - 0.7.7-7
- Add SCL macros

* Tue Jun 17 2014 Vít Ondruch <vondruch@redhat.com> - 0.7.7-6
- Fix FTBFS in Rawhide (rhbz#1107180).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Mar 07 2013 Vít Ondruch <vondruch@redhat.com> - 0.7.7-3
- Rebuild for https://fedoraproject.org/wiki/Features/Ruby_2.0.0

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 12 2012 Vít Ondruch <vondruch@redhat.com> - 0.7.7-1
- Update to netrc 0.7.7.

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 14 2012 Bohuslav Kabrda <bkabrda@redhat.com> - 0.7.1-1
- Update to latest upstream, which incorporates the added license.

* Thu Mar 08 2012 Vít Ondruch <vondruch@redhat.com> - 0.7-1
- Initial package
